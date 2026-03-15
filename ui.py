import streamlit as st
import requests
import uuid
import time

st.set_page_config(page_title="FAQ Chatbot")

st.title("🤖 Smart FAQ Chatbot")

# CLEAR CHAT BUTTON
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

API_URL = "http://127.0.0.1:8000/chat"

# create session id
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []


# STREAMING FUNCTION
def stream_data(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.03)


# display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# user input
prompt = st.chat_input("Ask a question")

if prompt:

    # show user message
    st.chat_message("user").write(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # call FastAPI backend
    response = requests.post(
        API_URL,
        json={
            "session_id": st.session_state.session_id,
            "question": prompt
        }
    )

    answer = response.json()["answer"]

    # show bot response with streaming
    with st.chat_message("assistant"):
        st.write_stream(stream_data(answer))

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )