import requests
import streamlit as st

st.set_page_config(
    page_title="RAG Assistant", page_icon="🤖", layout="centered"
)
st.title("🤖 Agentic RAG Knowledge Assistant")

# Your live n8n Cloud webhook endpoint
CHAT_WEBHOOK_URL = "https://bhagat2004.app.n8n.cloud/webhook/2c90dee0-e7fb-4a7c-9c38-cebd1d3285b3/chat"

# Maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User prompt
user_input = st.chat_input("Ask a question about your documents or URLs...")

if user_input:
    # Display user query
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Post to n8n chat trigger
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    CHAT_WEBHOOK_URL,
                    json={"chatInput": user_input},
                    headers={"Content-Type": "application/json"},
                    timeout=90,
                )

                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("output", "No response text received.")
                    st.markdown(answer)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                else:
                    err = f"Error {response.status_code}: {response.text}"
                    st.error(err)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": err}
                    )

            except requests.exceptions.RequestException as ex:
                err = f"Connection failed: {ex}"
                st.error(err)
                st.session_state.messages.append(
                    {"role": "assistant", "content": err}
                )
