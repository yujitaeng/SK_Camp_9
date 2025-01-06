import streamlit as st

st.title('오늘은 신나는 금요일!')
st.header('오늘은 Streamlit 배우는 날~')
st.subheader('Streamlit으로 만들어보자자')

# 문자열 박스를 만드는 input
my_site = st.text_input('오늘 내가 만들어보고 싶은 사이트는?')
# 문자열 박스에서 입력받은 것을 보여주는
st.write(my_site)

# 버튼 형성
if st.button(f'{my_site} 접속하기'):
    st.success(f'{my_site}로 접속 중', icon="🎶")