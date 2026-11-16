import streamlit as st

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("🔒 이 페이지는 로그인 후 접근할 수 있습니다. 메인 화면에서 로그인을 먼저 해주세요.")
    st.stop()

st.title("03 / IRIS LAB - 붓꽃 분류 실험실")
st.write("SVM(서포트 벡터 머신) 알고리즘을 이용해 꽃받침과 꽃잎 크기를 기반으로 붓꽃 종을 정밀 예측하는 시뮬레이터 공간입니다.")
