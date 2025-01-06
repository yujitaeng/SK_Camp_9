import pandas as pd
import streamlit as st
import numpy as np

st.subheader('나의 발자취')

df = pd.DataFrame(
    np.random.randn(300, 2) / [70, 70] + [37.5665, 126.9780],
    columns=["lat", "lon"],
)
st.map(df, size=10, color="#ff6a13")

st.text('')

df = pd.DataFrame(
    {
        "가게명": ["현선이네 떡볶이", "마부자김치찌개", "김밥천국국"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"]
    }
)

sentiment_mapping = [1, 2, 3, 4, 5]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"내 평점은?: {sentiment_mapping[selected]}")

st.dataframe(
    df,
    column_config={
        "가게명": "가게명",
        "url": st.column_config.LinkColumn("App URL")
    },
    hide_index=True,
)