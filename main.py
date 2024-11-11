import streamlit as st

# 페이지 선택 사이드바 생성
st.sidebar.title("메인 화면")
menu = st.sidebar.radio("메뉴 선택", ["메인 화면", "대시보드", "과거 기록"])

# 메인 화면
if menu == "메인 화면":
    st.title("메인 화면")
    
    # 레이아웃 설정 (영상, 결함 종류 통계)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("영상")
        st.image("https://via.placeholder.com/300", width=300)  # 여기에 실제 비디오 소스를 추가 가능
    with col2:
        st.write("결함 통계")
        st.bar_chart({"불량": [5], "OK": [20]})

    # 결함 종류 표시
    st.button("이전")
    st.button("다음")

    # 두부 이미지 및 결함 안내 표시
    col3, col4, col5 = st.columns(3)
    col3.write("현재 두부 사진")
    col4.write("결함 위치 크롭")
    col5.write("결함 안내")

# 대시보드
elif menu == "대시보드":
    st.title("대시보드")

# 과거 기록
elif menu == "과거 기록":
    st.title("과거 기록")
