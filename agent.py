from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

class Classification(BaseModel):
    category: Literal["Bug", "Feature Request", "General Query"]
    response_draft: str

class AgentState(TypedDict):
    ticket_text: str
    category: str
    response: str

def classify_and_draft(state: AgentState) -> AgentState:
    prompt = f"""You are a support agent. Analyze the ticket below and:
1. Classify it into one of: Bug, Feature Request, General Query.
2. Draft a friendly, professional first response.

Ticket: {state['ticket_text']}
"""
    structured_llm = llm.with_structured_output(Classification)
    result = structured_llm.invoke([HumanMessage(content=prompt)])
    state['category'] = result.category
    state['response'] = result.response_draft
    return state

workflow = StateGraph(AgentState)
workflow.add_node("analyze", classify_and_draft)
workflow.set_entry_point("analyze")
workflow.add_edge("analyze", END)
app = workflow.compile()

def run_agent(ticket_text: str) -> dict:
    return app.invoke({"ticket_text": ticket_text})
