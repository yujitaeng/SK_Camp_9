import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import base64
import openai
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 음성 인식 함수
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("말씀해주세요...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ko-KR")
        return text
    except sr.UnknownValueError:
        return "음성을 인식하지 못했습니다."
    except sr.RequestError:
        return "음성 인식 서비스에 접근할 수 없습니다."

# GPT-4o-mini를 이용한 응답 생성 함수
def generate_response(prompt):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 친절하고 도움이 되는 AI 어시스턴트입니다."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 텍스트를 음성으로 변환하는 함수
def text_to_speech(text):
    fd, temp_path = tempfile.mkstemp(suffix=".mp3")
    try:
        tts = gTTS(text=text, lang='ko')
        tts.save(temp_path)
        with open(temp_path, 'rb') as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        return audio_tag
    finally:
        os.close(fd)
        try:
            os.unlink(temp_path)
        except PermissionError:
            pass  # 파일 삭제 실패 시 무시

# Streamlit 앱 시작
st.set_page_config(page_title="음성 대화형 AI 챗봇", page_icon="🎙️", layout="wide")

st.title("🗣️ 음성 대화형 AI 챗봇")

# 세션 상태 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 3분할 레이아웃 생성 (2:1 비율)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 실시간 대화")
    # 음성 입력 버튼
    if st.button("🎤 음성으로 질문하기"):
        user_input = speech_to_text()
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.write(f"👤 사용자: {user_input}")

        # AI 응답 생성
        ai_response = generate_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.write(f"🤖 AI: {ai_response}")

        # AI 응답을 음성으로 출력
        audio_tag = text_to_speech(ai_response)
        st.markdown(audio_tag, unsafe_allow_html=True)

with col2:
    st.subheader("📜 대화 기록")
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(f"👤 **사용자**: {message['content']}")
        else:
            st.markdown(f"🤖 **AI**: {message['content']}")

# 스타일 적용
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff6a13;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 12px;
    }
    .stAudio {
        margin-top: 20px;
    }
    .css-1d391kg {
        padding-right: 1rem;
    }
</style>
""", unsafe_allow_html=True)
