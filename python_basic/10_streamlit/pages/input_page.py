import streamlit as st

# 제목
st.title('사용자 입력 받기')

col1, col2 = st.columns(2)

with col1:
    nickname = st.text_input('닉네임 입력') # 문자 입력
    age = st.number_input('나이 입력', min_value=13, max_value=80) #숫자 +- 로 조절하는

    options = ['대학생', '고등학생', '중학생', '초등학생']
    selected = st.selectbox('학교 입력', options) # 객관식 고르듯이

    r_options = ['맛집탐방', '영화 감상', '음악 감상', '사진찍기']
    choice = st.radio('취미 입력', r_options) # 동그란 원안의 체크 선택지
    selected_many = st.multiselect('취미가 여러개라면?', r_options) # 중복값 체크 선택지 (약간 태그박스같이 생긴)

    checked =st.checkbox('개인정보 제공 동의') # 체크박스 

with col2:
    if st.button('입력 완료!'):
        st.write(f'이름이 뭐야?{nickname}')
        st.write(f'몇 살이야? {age}')
        st.write(f'어디 다녀? {selected}')
        st.write(f'취미가 뭐야? {choice}')
        st.write(f'취미가 여러개야? {selected_many}')
        st.write(f'개인정보 제공 동의해? {checked}')