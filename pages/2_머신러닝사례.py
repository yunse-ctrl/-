import streamlit as st

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("🔒 이 페이지는 로그인 후 접근할 수 있습니다. 메인 화면에서 로그인을 먼저 해주세요.")
    st.stop()

st.title("02 / APPLICATIONS - 우리 주변의 머신러닝")
st.write("스팸 분류, 콘텐츠 추천, 음성 인식, 전력 수요 예측 등 다양한 산업과 일상에서 사용되는 AI 응용 사례를 탐구합니다.")
