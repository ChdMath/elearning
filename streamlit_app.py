import streamlit as st

# ---------- Khởi tạo session ----------
if "role" not in st.session_state:
    st.session_state.role = None
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "model" not in st.session_state:
    st.session_state.model = "gpt-3.5-turbo"
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Chọn vai trò ----------
st.title("🎓 Nền tảng học tập sử dụng AI")

role = st.sidebar.selectbox("🔐 Chọn vai trò", ["Học sinh", "Giáo viên", "Admin"])

# ---------- Vai trò ADMIN ----------
if role == "Admin":
    st.header("👑 Cài đặt AI từ Admin")
    st.session_state.role = "admin"

    api = st.text_input("🔑 Nhập API Key", value=st.session_state.api_key, type="password")
    model = st.selectbox("🧠 Chọn mô hình", ["gpt-3.5-turbo", "gpt-4", "Claude", "Gemini"])
    curl_example = f"""curl https://api.openai.com/v1/chat/completions \\
  -H "Authorization: Bearer {api}" \\
  -H "Content-Type: application/json" \\
  -d '{{"model": "{model}", "messages": [{{"role":"user","content":"Xin chào"}}]}}'
"""

    if st.button("💾 Lưu cài đặt"):
        st.session_state.api_key = api
        st.session_state.model = model
        st.success("✅ Đã lưu API key và model.")

    st.subheader("📋 CURL mẫu:")
    st.code(curl_example, language="bash")

# ---------- Vai trò HỌC SINH ----------
elif role == "Học sinh":
    st.header("🤖 Hỏi đáp cùng AI")
    st.session_state.role = "student"

    if not st.session_state.api_key:
        st.warning("Admin chưa cài đặt API key.")
    else:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_input = st.chat_input("Nhập câu hỏi của bạn...")
        if user_input:
            # Lưu tin nhắn
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Gọi API thật ở đây (tạm phản hồi giả)
            with st.chat_message("assistant"):
                fake_reply = f"[Mô hình: {st.session_state.model}] Trả lời: Tôi đang xử lý câu hỏi của bạn..."
                st.markdown(fake_reply)
                st.session_state.messages.append({"role": "assistant", "content": fake_reply})

# ---------- Vai trò GIÁO VIÊN ----------
elif role == "Giáo viên":
    st.header("📚 Quản lý nội dung (Giáo viên)")
    st.session_state.role = "teacher"
    st.info("Chức năng cho giáo viên sẽ được cập nhật sau.")
