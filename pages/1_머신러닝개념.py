import streamlit as st

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("🔒 이 페이지는 로그인 후 접근할 수 있습니다. 메인 화면에서 로그인을 먼저 해주세요.")
    st.stop()

st.title("01 / CONCEPT - 머신러닝의 핵심")
st.markdown('''
**머신러닝(Machine Learning)**은 사람이 모든 판단 규칙을 직접 작성하는 대신,
컴퓨터가 **데이터에서 패턴을 학습해 새로운 입력을 예측하거나 분류**하게 하는 인공지능 기술입니다.
학습한 결과물은 **모델**이라고 부릅니다.
''')
