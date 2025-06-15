import os
from dotenv import load_dotenv

import streamlit as st
import difflib

from langchain_openai import ChatOpenAI

KEYWORD_RESPONSES = {
        "hello": "Hello! How can I assist you today?",
        "help": "Sure, I'm here to help. Please describe your issue.",
        "price": "Our pricing information can be found on our website.",
        "support": "You can contact support at support@example.com.",
        "bye": "Goodbye! Have a great day!",
        "order": "For order-related inquiries, please visit our order help page.",
        "account": "For account-related issues, please visit our account help page.",
        "payment": "For payment issues, please check our payment help section.",
        "shipping": "Shipping information can be found on our shipping page.",
        "default": "I'm sorry, I didn't understand that.\n\n I can help you with account, order, shipping or payment issues.\n\nCan you please rephrase?",
    }

SIMILAR_KEYWORDS = {
        "hello": ["hello", "helo", "hey", "hi", "hullo"],
        "help": ["help", "halp", "assist", "support"],
        "price": ["price", "cost", "fee", "prize", "pricing"],
        "support": ["support", "assistance", "helpdesk"],
        "bye": ["bye", "goodbye", "see ya", "cya"],
        "order": ["order", "purchase", "buy", "place order"],
        "account": ["account", "profile", "user account", "my account"],
        "payment": ["payment", "pay", "billing", "charge"],
        "shipping": ["shipping", "delivery", "ship", "postage"],
    }

def header():
    st.set_page_config(page_title="Keyword Based Chatbot", page_icon=":abc:")
    st.title("Keyword Based Chatbot")
    st.write("This page is dedicated to the keyword based chatbot.")
    st.session_state.use_ai = st.selectbox(
        "Enable AI for smarter keyword matching? (e.g., if 'Yes', typing 'Holla' will use AI to find the closest keyword match)",
        options=["No", "Yes"],
        index=0,
    )
    load_dotenv()

def main():
    st.subheader("Interact with the keyword based chatbot")

    init()

def init():
    if "use_ai" not in st.session_state:
        st.session_state.use_ai = "No"
    
    if "keyword_based_messages" not in st.session_state:
        st.session_state.keyword_based_messages = [
            ("assistant", "How may I assist you today?\n\nI can help you with account, order, shipping or payment issues."),
        ]

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.keyword_based_messages.append(("user", user_input))
        response = get_response(user_input)
        st.session_state.keyword_based_messages.append(("assistant", response))

    for sender, message in st.session_state.keyword_based_messages:
        with st.chat_message(sender):
            st.markdown(message)

def get_response(user_input):
    if st.session_state.use_ai == "Yes":
        user_input = ai_keyword_similarity(user_input)
    else:
        user_input = user_input.lower()

    words = user_input.split()
    best_match = None
    best_ratio = 0.0
    best_keyword = None

    for keyword, variants in SIMILAR_KEYWORDS.items():
        for variant in variants:
            for word in words:
                ratio = difflib.SequenceMatcher(None, word, variant).ratio()
                if ratio > best_ratio and ratio > 0.9:
                    best_ratio = ratio
                    best_keyword = keyword
            if variant in user_input:
                best_keyword = keyword
                best_ratio = 1.0

    if best_keyword:
        return KEYWORD_RESPONSES[best_keyword]
    return KEYWORD_RESPONSES["default"]

def ai_keyword_similarity(user_input):
    llm = ChatOpenAI(model="gpt-4.1-nano")
    message = [
        (
            "system",
            "You are a keyword-based chatbot assistant. Your task is to classify the user's message into one of the following categories: hello, help, price, support, bye, order, account, payment, shipping, or default. "
            "Respond with only the single category word (e.g., 'hello', 'help', etc.) that best matches the user's input. "
            "If the input does not fit any category, respond with 'default'. Do not provide any explanation or additional text. Just return the category word.",
        ),
        (
            "human",
            user_input
        )
    ]
    matched_keyword = llm.invoke(message).content.strip()

    return matched_keyword if matched_keyword in KEYWORD_RESPONSES else "default"

header()
main()