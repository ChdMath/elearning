import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(page_title="Hệ thống quản lý học tập", layout="wide")

st.title("📚 Hệ thống Quản Lý Học Tập")

# Load file HTML đã thiết kế
html_path = pathlib.Path("assets/dashboard.html")
if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        components.html(html_content, height=1000, scrolling=True)
else:
    st.error("❌ Không tìm thấy file giao diện HTML. Kiểm tra 'assets/dashboard.html'")
