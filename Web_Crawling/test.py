import streamlit as st

# 두 개의 열 생성
col1, col2 = st.columns([3, 1])  # 비율 조정 가능

# 첫 번째 열에 텍스트 입력 창 추가
with col1:
    user_input = st.text_input("검색어를 입력하세요", label_visibility="collapsed")  # 라벨 숨기기

# 두 번째 열에 버튼 추가
with col2:
    search_btn = st.button("검색")

# 버튼 클릭 시 동작
if search_btn:
    st.write(f"입력한 검색어: {user_input}")
