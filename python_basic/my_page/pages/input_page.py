import streamlit as st
from datetime import time


st.title('맛집 지도')

# 인원
st.subheader('방문 인원은?', divider="gray")
people = st.slider("방문 인원", 0, 20, 2)
st.write(f'{people}명 방문 희망')

# 예산
st.subheader('오늘의 한 끼 비용은?', divider="gray")
budget = st.slider("예산", 5000, 100000, (10000, 50000))
st.write("오늘의 한 끼 비용:", budget)

# 도보 몇 분까지 (반경거리)
st.subheader('도보 몇 분까지 이동하시나요?', divider="gray")
time = ["5분 이내", "10분", "15분", "20분 이상"]
selection = st.pills("도보 이동 시간", time)
st.markdown(f"선택한 도보 이동 시간: {selection}")

# 후기
st.subheader('어느 정도 후기의 맛집을 찾고 계신가요?', divider="gray")
Reviews = st.slider("후기", 1.0, 5.0, (3.8, 5.0))
st.write(f'{Reviews}정도면 도전해볼만하다!')

# 고려옵션
st.subheader('어떤 장소를 찾고 계신가요?', divider="gray")
options = ['룸', '금연', '노키즈존', '주차장', '예약', '반려동물(소/중형견)', '배달', '반려동물(대형견)', '키즈존']
seleted_options = st.pills("옵션", options, selection_mode="multi")
st.markdown(f"선택한 옵션 {seleted_options}")
