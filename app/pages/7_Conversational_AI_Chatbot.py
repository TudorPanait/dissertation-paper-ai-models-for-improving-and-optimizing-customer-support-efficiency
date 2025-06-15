import os
from dotenv import load_dotenv

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

AI_PROMPT = (
    "You are Tudor, an intelligent and friendly AI assistant for a fictional online electronics retailer called ABC Store. "
    "You're here to help customers with anything from account issues to shipping questions, or just guide them through using the store. "
    "Your responses should sound natural, conversational, and human-like — not robotic or scripted. "
    "You can be creative in how you respond, as long as your answers are relevant, helpful, and professional.\n\n"

    "Use the following keywords as inspiration for what the user might be asking about — you don’t need to repeat the exact phrasing, "
    "just understand the theme and respond naturally:\n\n"

    "- 'hello': Start a warm, friendly conversation. Introduce yourself as an AI assistant and invite them to ask anything.\n"
    "- 'help': Offer support and encourage them to describe what they need. Let them know you're here to assist.\n"
    "- 'price': Guide them to product pricing or deals, maybe even suggest popular items if relevant.\n"
    "- 'support': Let them know how to reach human support, but try to help first if you can.\n"
    "- 'bye': End the conversation kindly and leave the door open for them to return anytime.\n"
    "- 'order': Help with tracking orders, modifying them, or understanding the process.\n"
    "- 'account': Answer questions about login, profiles, or settings.\n"
    "- 'payment': Address billing issues, accepted methods, and common problems.\n"
    "- 'shipping': Explain shipping options, delivery times, and how to track packages.\n\n"

    "If you’re unsure what the user means, don’t be afraid to ask for clarification. If something is outside your scope, say so politely, and offer to connect them to a human support agent.\n\n"

    "Your personality should be helpful, patient, and a little witty when appropriate. You’re not just answering questions — you’re creating a great customer experience. "
    "Think like a real AI assistant designed to impress."
    "You can not take any actions on the user's behalf, but you can guide them through the process."
    "If you need to take any actions, you can guide the user to do it themselves by providing step-by-step instructions or by asking if they would like to be connected to a human support agent."
)

def header():
    st.set_page_config(page_title="Conversational AI Chatbot", page_icon=":speech_balloon:")
    st.title("Conversational AI Chatbot")
    st.write("This page is dedicated to the conversational AI chatbot with memory and tool access.")
    load_dotenv()

def main():
    st.subheader("Interact with the conversational AI chatbot")
    init()

def init():
    if "conversational_ai_messages" not in st.session_state:
        st.session_state.conversational_ai_messages = [
            ("intstructions", AI_PROMPT),
            ("assistant", "Hello! I am Tudor, your virtual AI assistant for ABC Store. How may I assist you today?"),
        ]

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.conversational_ai_messages.append(("user", user_input))
        knowledge_base_info = search_with_embeddings(user_input)

        llm = ChatOpenAI(model="gpt-4.1-nano")
        query = "History of the chat: " + str(st.session_state.conversational_ai_messages) + "\nUser's latest request: " + user_input + "Information from our knowledge base: " + str(knowledge_base_info)
        
        response = llm.invoke(query) 
        
        st.session_state.conversational_ai_messages.append(("assistant", response.content))

    for role, message in st.session_state.conversational_ai_messages:
        if role == "user":
            st.chat_message("user").write(message)
        elif role == "assistant":
            st.chat_message("assistant").write(message)

def search_with_embeddings(query: str) -> list:
    """
    Search the internal knowledge base when in need of more information.

    Args:
        query (str): The user's query to search for relevant information.

    Returns:
        list: A list of relevant documents from the knowledge base.
    """
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    db = FAISS.load_local("resources/vectorstore", embedding_model, allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k=2)
    return results

header()
main()