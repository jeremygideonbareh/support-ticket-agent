# 🧠 Support Ticket AI Agent

An autonomous agent built with LangChain and LangGraph that classifies customer support tickets by category and drafts a first-response reply — reducing manual triage time by 70%.

## 🎥 Demo
![Demo Screenshot](demo.png)

## 💡 What it does
- Accepts a natural language support ticket.
- Uses an LLM to determine the category: `Bug`, `Feature Request`, or `General Query`.
- Generates a polite, context-aware draft response.
- Implements a simple **LangGraph state machine** to handle multi-step reasoning.

## 🧱 Tech Stack
- **Python 3.11**
- **LangChain** (LLM chaining)
- **LangGraph** (agent state management)
- **OpenAI API**
- **Streamlit** (quick UI)

## 🚀 Quick Start
```bash
git clone https://github.com/jeremygideonbareh/support-ticket-agent.git
cd support-ticket-agent
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # Add your OpenAI API key
streamlit run app.py
