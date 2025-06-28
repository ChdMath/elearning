import streamlit as st
import random

# --- Cấu hình trang ---
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 Trợ lý học tập AI")

# --- Giới thiệu ngắn ---
with st.expander("📘 Hướng dẫn sử dụng", expanded=False):
    st.markdown("""
    - Nhập câu hỏi vào khung bên dưới.
    - AI sẽ trả lời như một trợ lý học tập.
    - Dữ liệu sẽ được giữ trong phiên hiện tại.
    """)

# --- Khởi tạo session state để lưu hội thoại ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Xin chào! Tôi có thể giúp gì cho bạn hôm nay?"}
    ]

# --- Hiển thị lịch sử hội thoại ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Người dùng nhập câu hỏi ---
prompt = st.chat_input("Nhập câu hỏi của bạn...")

# --- Hàm phản hồi AI đơn giản (giả lập) ---
def generate_ai_reply(user_input):
    fake_replies = [
        "Câu hỏi rất hay! Để tôi suy nghĩ chút nhé...",
        "Tôi nghĩ bạn nên bắt đầu từ chương 2.",
        "Hãy thử giải bài tập tương tự trong SGK.",
        "Tôi khuyên bạn tra cứu thêm tại VietJack hoặc Hocmai.",
        "Có thể bạn cần luyện thêm phần này. Tôi có thể giúp bạn nếu muốn!"
    ]
    return random.choice(fake_replies)

# --- Xử lý khi người dùng gửi tin nhắn ---
if prompt:
    # Lưu tin nhắn người dùng
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Tạo phản hồi từ AI (tạm thời dùng mẫu giả lập)
    ai_reply = generate_ai_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
