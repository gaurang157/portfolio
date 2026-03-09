import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide", page_title="Gaurang Ingle — Portfolio")

st.markdown("""
<style>
    header[data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

html_content = (Path(__file__).parent / "gaurang-ingle-portfolio.html").read_text(encoding="utf-8")

st.components.v1.html(html_content, height=1080, scrolling=True)
