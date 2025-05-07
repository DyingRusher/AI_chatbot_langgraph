import streamlit as st

st.set_page_config(page_title="Learn Langgraph",layout="wide",page_icon="a")
st.title("Ai chatbot langgraph")
st.write("chat with chatbot")

system_prompt = st.text_area("Define your ai agent" ,placeholder="Type your system prompt here")

model_name_groq = ["llama-3.3-70b-versatile",'llama3-8b-8192','mistral-saba-24b']
model_name_openai = ["gpt-4o-mini"]

provider = st.radio("Select your model provider",options=["groq","openai"],index=0)

if provider == "groq":
    model_name = st.selectbox("Select your model",options=model_name_groq)
else:
    model_name = st.selectbox("select your model",options = model_name_openai)

allow_search = st.checkbox("Allow web search",value=False)

user_prompt = st.text_area("Enter your prompt" ,placeholder="Type your prompt here")

API_URL = 'http://127.0.0.1:6969/chat'

if st.button("submit"):
    if user_prompt.strip:

        import requests

        payload = {
                "model_name": model_name,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages":[user_prompt],
                "allow_search": allow_search,
        }

        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Ai response")
                st.markdown(f"**final response:**{response_data})")
    