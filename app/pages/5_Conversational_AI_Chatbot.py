import os
from dotenv import load_dotenv

import streamlit as st
import difflib

from langchain_openai import ChatOpenAI

AI_PROMPT = (
    "You are Tudor, a virtual AI assistant for a fictive online electronic goods retailer called ABC Store. "
    "Your job is to help users with common support needs. Respond based on the following keywords and responses:\n"
    "- 'hello': 'Hello! How can I assist you today?'\n"
    "- 'help': 'Sure, I'm here to help. Please describe your issue.'\n"
    "- 'price': 'Our pricing information can be found on our website.'\n"
    "- 'support': 'You can contact support at support@example.com.'\n"
    "- 'bye': 'Goodbye! Have a great day!'\n"
    "- 'order': 'For order-related inquiries, please visit our order help page.'\n"
    "- 'account': 'For account-related issues, please visit our account help page.'\n"
    "- 'payment': 'For payment issues, please check our payment help section.'\n"
    "- 'shipping': 'Shipping information can be found on our shipping page.'\n"
    "If the user's input does not match any of these keywords, reply with: "
    "'I'm sorry, I didn't understand that. I can help you with account, order, shipping or payment issues. Can you please rephrase?'\n"
    "Always let the user know you are an AI assistant. If you are unsure or cannot fulfill a request, say you can't help and ask if they want to be connected to a human agent."
)

def header():
    st.set_page_config(page_title="Conversational AI Chatbot", page_icon=":speech_balloon:")
    st.title("Conversational AI Chatbot")
    st.write("This page is dedicated to the conversational AI chatbot.")
    st.warning("🚧 This feature is a Work In Progress (WIP).", icon="⚠️")
    load_dotenv()

def main():
    st.subheader("Interact with the conversational AI chatbot")

    init()

def init():
    if "conversational_ai_messages" not in st.session_state:
        st.session_state.conversational_ai_messages = [
            ("assistant", "Hello! I am Tudor, your virtual AI assistant for ABC Store. How may I assist you today?"),
        ]

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.conversational_ai_messages.append(("user", user_input))

        llm = ChatOpenAI(model="gpt-4.1-nano")
        response = llm.invoke(AI_PROMPT + "\nUser: " + user_input)
        st.session_state.conversational_ai_messages.append(("assistant", response.content))

    for role, message in st.session_state.conversational_ai_messages:
        if role == "user":
            st.chat_message("user").write(message)
        else:
            st.chat_message("assistant").write(message)

header()
main()