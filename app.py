import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Support AI Agent", layout="centered")
st.title("🤖 Support Ticket AI Agent")
ticket = st.text_area("Paste a support ticket:", height=200)
if st.button("Analyze"):
    if ticket:
        with st.spinner("Agent thinking..."):
            result = run_agent(ticket)
        st.success(f"**Category:** {result['category']}")
        st.info(f"**Suggested Response:**\n\n{result['response']}")
    else:
        st.warning("Please enter a ticket.")
