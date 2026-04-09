from dotenv import load_dotenv
import os
from datetime import datetime

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
import gradio as gr

load_dotenv()

def get_date():
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")

llm = ChatOllama(model="qwen3-vl:4b")

system_prompt = """ 
You are a helpful assistant.
Answer all user's queries.
Use the get_date tool if the user is asking about the today's date.
"""

agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)

def chat(message, history):
    response = agent.invoke({"messages":[{"role":"user", "content": message}]})
    last_response = response['messages'][-1].content
    return last_response
#print(response['messages'][-1].content)

with gr.Blocks() as demo:
    gr.Markdown("# AI Chatbot")
    gr.ChatInterface(fn=chat)

demo.launch()

