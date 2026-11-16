import streamlit as st
import sqlite3
from datetime import datetime
import pytz

# Page configuration
st.set_page_config(page_title="AX 교육 분석 시스템", page_icon="💻", layout="wide")

# Database initialization
def get_db_connection():
    conn = sqlite3.connect("myproject.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT NOT NULL,
            userid TEXT NOT NULL UNIQUE,
            passwd TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    # Inventory table for survey
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            userid TEXT NOT NULL,
            q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER,
            q6 INTEGER, q7 INTEGER, q8 INTEGER, q9 INTEGER, q10 INTEGER,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Session State for tracking user login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "userid" not in st.session_state:
    st.session_state["userid"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None

# Sidebar Navigation Control / Custom Survey Access
def check_login():
    if not st.session_state["logged_in"]:
        st.sidebar.warning("로그인 후 이용 가능합니다.")
        return False
    return True

# Helper to get KST time string
def get_kst_now():
    kst = pytz.timezone('Asia/Seoul')
    return datetime.now(kst).strftime('%Y-%m-%d %H:%M:%S')

# Authentication UI inside Landing Page (Tabs)
st.title("💻 AX 전환 교육 플랫폼")

if not st.session_state["logged_in"]:
    tab1, tab2 = st.tabs(["🔒 로그인", "📝 신규 회원가입"])
    
    with tab1:
        st.subheader("로그인")
        login_id = st.text_input("아이디", key="login_id")
        login_pw = st.text_input("비밀번호", type="password", key="login_pw")
        if st.button("로그인 실행"):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE userid = ? AND passwd = ?", (login_id, login_pw))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                st.session_state["logged_in"] = True
                st.session_state["userid"] = user["userid"]
                st.session_state["username"] = user["username"]
                st.success(f"{user['username']}님, 환영합니다!")
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 잘못되었습니다.")
                
    with tab2:
        st.subheader("신규 가입")
        new_name = st.text_input("이름", key="new_name")
        new_id = st.text_input("아이디(중복 불가)", key="new_id")
        new_pw = st.text_input("비밀번호", type="password", key="new_pw")
        
        if st.button("회원가입 완료"):
            if new_name and new_id and new_pw:
                try:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    now_str = get_kst_now()
                    cursor.execute(
                        "INSERT INTO users (username, userid, passwd, created_at) VALUES (?, ?, ?, ?)",
                        (new_name, new_id, new_pw, now_str)
                    )
                    conn.commit()
                    conn.close()
                    st.success("회원가입이 완료되었습니다! 로그인 탭에서 로그인을 진행해 주세요.")
                except sqlite3.IntegrityError:
                    st.error("이미 존재하는 아이디입니다.")
            else:
                st.error("모든 항목을 입력해 주세요.")
else:
    # Authenticated Landing Page View
    st.sidebar.markdown(f"**🟢 {st.session_state['username']}님 로그인 중**")
    if st.sidebar.button("로그아웃"):
        st.session_state["logged_in"] = False
        st.session_state["userid"] = None
        st.session_state["username"] = None
        st.rerun()
        
    st.info("성공적으로 로그인되었습니다. 왼쪽 사이드바 메뉴 또는 하단의 실태조사를 시작해 보세요!")
    
    # 5. Inventory Survey UI Section
    st.markdown("---")
    st.header("📋 AX 전환에 따른 학생 인식 실태조사")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE userid = ?", (st.session_state["userid"],))
    already_done = cursor.fetchone()
    conn.close()
    
    if already_done:
        st.success("✅ 이미 실태조사에 참여하셨습니다. 참여해 주셔서 감사합니다!")
    else:
        st.write("인공지능 전환(AX) 교육 환경 변화에 대한 여러분의 인식을 조사합니다. 각 문항에 성실히 답해 주세요. (1: 매우 아니다 ~ 5: 매우 그렇다)")
        
        questions = [
            "Q1. 인공지능 전환(AX) 교육이 미래 학업 및 커리어에 필수적이라고 생각한다.",
            "Q2. 학교의 AX 교육 인프라(AI 도구, 소프트웨어 등)는 충분히 제공되고 있다.",
            "Q3. AI 기반 학습 도구(ChatGPT, 시뮬레이터 등)를 수업에 활용하는 데 자신감이 있다.",
            "Q4. AX 전환 이후 수업 방식이 이전보다 더 효율적이고 몰입도가 높아졌다.",
            "Q5. 디지털 플랫폼을 통한 맞춤형 개별 학습이 나의 학습 능력을 향상시킨다.",
            "Q6. AX 교육을 원활히 수강하기 위해 스스로 디지털 역량을 계속 키우고 있다.",
            "Q7. 수업 중 AI 기술 활용에 따른 개인정보 유출이나 보안 문제가 우려된다.",
            "Q8. AI가 제공하는 지식이나 평가 결과를 전적으로 신뢰할 수 있다.",
            "Q9. AX 교육 환경에서 교수자와 학생 간의 정서적 교감이나 상호작용이 약화될까 봐 우려된다.",
            "Q10. 앞으로 전공 교육 전반에 걸쳐 AX 기술 접목 수업이 더 확대되어야 한다."
        ]
        
        with st.form("survey_form"):
            responses = []
            for i, q in enumerate(questions):
                res = st.radio(q, [1, 2, 3, 4, 5], index=2, horizontal=True, key=f"q_ans_{i+1}")
                responses.append(res)
                
            submitted_survey = st.form_submit_button("설문 제출하기")
            if submitted_survey:
                conn = get_db_connection()
                cursor = conn.cursor()
                now_str = get_kst_now()
                cursor.execute(
                    '''INSERT INTO inventory (userid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, created_at) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    [st.session_state["userid"]] + responses + [now_str]
                )
                conn.commit()
                conn.close()
                st.success("🎉 설문 조사가 성공적으로 저장되었습니다!")
                st.rerun()
