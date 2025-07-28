import streamlit as st
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()

from orchestrator import MyAgentOrchestrator  # our wrapper from step 2

# ✅ Initialize orchestrator only once
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = MyAgentOrchestrator()

# ✅ Store conversation history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🏃‍♂️ Training Coach Agent (ADK)")

# Display previous chat history
for msg in st.session_state.history:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input field
user_query = st.chat_input("Ask me about your training, research, or planning...")

if user_query:
    # Add user message
    st.session_state.history.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    # Run the ADK orchestrator
    with st.spinner("Thinking..."):
        response = st.session_state.orchestrator.run(user_query)

    # Add assistant response
    st.session_state.history.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
