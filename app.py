import streamlit as st
from google import genai

# 🔑 SECURE 
api_key = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=api_key)


st.set_page_config(page_title="Gemini AI App", page_icon="🤖")

st.title("🤖 Gemini AI Chat App")

# Input
prompt = st.text_area("Enter your prompt")

# Button
if st.button("Generate Response"):

    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        try:
            with st.spinner("Thinking... 🤔"):
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash-lite",
                    contents=prompt
                )

            st.success("Done!")
            st.subheader("Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error occurred: {e}")