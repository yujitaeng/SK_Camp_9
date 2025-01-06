import streamlit as st

# 데이터: 리스트와 딕셔너리를 사용한 가상의 검색 데이터베이스
data = [
    {
        "Title": "Streamlit Guide",                     # 제목
        "Description": "A comprehensive guide to Streamlit.",  # 설명
        "URL": "https://docs.streamlit.io"              # 링크
    },
    {
        "Title": "Learn Python",                        # 제목
        "Description": "Learn Python programming for beginners and experts.",  # 설명
        "URL": "https://python.org"                    # 링크
    }
    # ...다른 항목들
]


# CSS 스타일 적용: 중앙 정렬
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .search-input {
        margin-top: 20px;
        width: 50%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 중앙 정렬 컨테이너
with st.container():
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # 페이지 제목
    st.title("전기차톡⚡")

    # 검색창
    keyword = st.text_input("검색어를 입력해주세요:", "")

    if keyword:
        # 검색 결과 필터링
        results = [item for item in data if keyword.lower() in item["Title"].lower() or keyword.lower() in item["Description"].lower()]

        # 결과 표시
        if results:
            st.subheader(f"'{keyword}'에 대한 검색 결과입니다:")
            for item in results:
                st.markdown(f"### [{item['Title']}]({item['URL']})")
                st.write(item["Description"])
                st.write("---")
        else:
            st.warning(f"'{keyword}'에 대한 정보가 없습니다. 다시 입력해주세요😥")
    else:
        st.info("잠시만 기다려 주시면 조회 결과를 안내해 드리겠습니다🚗💨")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("Made with Team 4 Avengers.")
