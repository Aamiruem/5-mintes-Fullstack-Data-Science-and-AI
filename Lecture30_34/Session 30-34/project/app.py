# import streamlit as st
# import google.generativeai as genai

# # Page config
# st.set_page_config(page_title="AI Q&A", page_icon="🤖")

# # Title
# st.title("🤖 Question-Answers App")

# # Safe API key handling
# try:
#     genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# except Exception:
#     st.error("⚠️ API Key not found. Please add it in .streamlit/secrets.toml")
#     st.stop()

# # Load model
# model = genai.GenerativeModel("gemini-1.5-flash-latest")

# # User input
# user_input = st.text_area("Enter Your Question", placeholder="Ask anything...")

# # Button
# if st.button("Answer"):
#     if user_input.strip() == "":
#         st.warning("⚠️ Please enter a question")
#     else:
#         try:
#             with st.spinner("Thinking... 🤔"):
#                 response = model.generate_content(user_input)

#             # Handle empty response safely
#             if response and hasattr(response, "text"):
#                 st.success(response.text)
#             else:
#                 st.error("⚠️ No response from model")

#         except Exception as e:
#             st.error(f"❌ Error: {str(e)}")


import streamlit as st
import google.generativeai as genai

st.title("Question-Answers")

# API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# ✅ Correct model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

user_input = st.text_area("Enter Your Question")

if st.button("Answer"):
    if user_input.strip():
        try:
            with st.spinner("Thinking..."):
                response = model.generate_content(user_input)
            st.success(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a question")
