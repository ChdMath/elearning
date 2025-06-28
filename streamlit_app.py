import streamlit as st

# Khởi tạo session state nếu chưa có
if "ai_provider" not in st.session_state:
    st.session_state.ai_provider = "gemini"
if "api_config" not in st.session_state:
    st.session_state.api_config = {}

# Layout
st.set_page_config(page_title="Quản trị AI - Homework Helper", layout="wide")
st.title("👑 Trang quản trị - Cài đặt AI cho hệ thống")

# --- Chọn loại AI ---
st.subheader("🔧 Chọn nhà cung cấp AI")

ai_option = st.radio("Nhà cung cấp", ["gemini", "openrouter", "openai", "custom"], index=0, horizontal=True)
st.session_state.ai_provider = ai_option

with st.form("ai_config_form"):
    st.markdown(f"### ⚙️ Cấu hình cho **{ai_option.upper()}**")

    if ai_option == "gemini":
        api_key = st.text_input("🔑 Gemini API Key", type="password")
        model = st.selectbox("📦 Chọn model", ["gemini-2.0-flash", "gemini-1.5-pro", "gemini-1.5-flash"])
        doc_link = "[🔗 Lấy API key tại Google AI Studio](https://makersuite.google.com/app/apikey)"

    elif ai_option == "openrouter":
        api_key = st.text_input("🔑 OpenRouter API Key", type="password")
        model = st.selectbox("📦 Chọn model", [
            "deepseek/deepseek-r1-0528:free",
            "openai/gpt-3.5-turbo", "openai/gpt-4", "anthropic/claude-3-sonnet"
        ])
        doc_link = "[🔗 Lấy API key tại OpenRouter](https://openrouter.ai/keys)"

    elif ai_option == "openai":
        api_key = st.text_input("🔑 OpenAI API Key", type="password")
        model = st.selectbox("📦 Chọn model", ["gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4-turbo"])
        doc_link = "[🔗 Lấy API key tại OpenAI Platform](https://platform.openai.com/api-keys)"

    elif ai_option == "custom":
        api_key = st.text_input("🔑 Custom API Key", type="password")
        model = st.text_input("🧠 Model (tuỳ chọn)", value="gpt-3.5-turbo")
        base_url = st.text_input("🌐 Base URL", placeholder="https://api.example.com/v1/chat/completions")
        headers = st.text_area("📄 Headers (JSON)", placeholder='{"Authorization": "Bearer sk-..."}')
        doc_link = "*Tuỳ chỉnh theo endpoint riêng.*"

    # Ghi chú bổ sung
    st.markdown(doc_link)

    submitted = st.form_submit_button("💾 Lưu cấu hình")
    if submitted:
        st.session_state.api_config[ai_option] = {
            "api_key": api_key,
            "model": model,
        }
        if ai_option == "custom":
            st.session_state.api_config[ai_option]["base_url"] = base_url
            st.session_state.api_config[ai_option]["headers"] = headers
        st.success("✅ Đã lưu cấu hình!")

# --- Hiển thị Curl mẫu ---
st.subheader("📋 CURL mẫu")

def render_curl():
    config = st.session_state.api_config.get(ai_option, {})
    api_key = config.get("api_key", "sk-...")
    model = config.get("model", "gpt-3.5-turbo")
    
    if ai_option == "custom":
        base_url = config.get("base_url", "https://api.example.com/v1/chat/completions")
    elif ai_option == "openrouter":
        base_url = "https://openrouter.ai/api/v1/chat/completions"
    elif ai_option == "openai":
        base_url = "https://api.openai.com/v1/chat/completions"
    elif ai_option == "gemini":
        base_url = "https://generativelanguage.googleapis.com/v1beta/models/chat:generateContent"

    curl_cmd = f"""curl {base_url} \\
  -H "Authorization: Bearer {api_key}" \\
  -H "Content-Type: application/json" \\
  -d '{{"model": "{model}", "messages": [{{"role":"user","content":"Xin chào"}}]}}'"""

    return curl_cmd

st.code(render_curl(), language="bash")

# --- Test API (giả lập) ---
st.subheader("🧪 Test kết nối API")
if st.button("🔄 Thử kết nối"):
    st.info(f"🔧 Đang thử gửi yêu cầu tới {ai_option.upper()}...")
    st.success("✅ Kết nối giả lập thành công (demo)")

