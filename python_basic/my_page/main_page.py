import streamlit as st

st.title('지금 내 주변엔?🍴')
st.header('"맛 없는 걸로 배채우는 건 기분이 나쁘니까 맛집만 찾아 갈래."')
st.subheader('내 주변에에 후기 3.8이상의 맛집을 찾아줄게요.')

my_site = st.text_input('지금 뭐 먹고 싶나요?')
st.write(my_site)

if st.button(f'{my_site} 맛집 찾기'):
    st.success(f"맛있는 냄새를 따라 내 주변의 '{my_site}맛집'을 찾는 중이에요.🐽", icon="🔎")