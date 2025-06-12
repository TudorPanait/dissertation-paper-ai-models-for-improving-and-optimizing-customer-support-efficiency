import os
from dotenv import load_dotenv

import streamlit as st

def header():
    st.set_page_config(page_title="Rule Based Chatbot", page_icon=":memo:")
    st.title("Rule Based Chatbot")
    st.write("This page is dedicated to the rule based chatbot.")
    load_dotenv()

def main():
    st.subheader("Interact with the rule based chatbot")

    init()

    # Level 1: Initial message
    if st.session_state.last_button == "Account Issues":
        write_message("user", "text", "I have an account issue, please help.")
        write_message("assistant", "text" , "Please select one of the following options.")
        write_message("assistant", "button", "Reset Password")
        write_message("assistant", "button", "Update Info")
    elif st.session_state.last_button == "Order Status":
        write_message("user", "text", "I want to check my order status, please.")
        write_message("assistant", "text", "Please select one of the following options.")
        write_message("assistant", "button", "Track Order")
        write_message("assistant", "button", "Cancel Order")
    elif st.session_state.last_button == "Talk to a Human Agent":
        write_message("user", "text", "I want to talk to a Human Agent, please.")
        write_message("assistant", "text", "Please wait while we connect you to a human agent.")

    # Level 2: Account Issues
    if st.session_state.last_button == "Reset Password":
        write_message("user", "text", "I want to reset my password.")
        write_message("assistant", "text", "Please follow this link to reset your password: [Reset Password Link]")
    elif st.session_state.last_button == "Update Info":
        write_message("user", "text", "I want to update my account information.")
        write_message("assistant", "text", "Please follow this link to update your information: [Update Info Link]")  

    # Level 2: Order Status
    if st.session_state.last_button == "Track Order":
        if st.session_state.user_input == "":
            write_message("user", "text", "I want to track my order.")
            write_message("assistant", "input", "Please enter your order ID to track your order.")
        elif st.session_state.user_input:
            write_message("user", "text", f"My order ID: {st.session_state.user_input}")
            write_message("assistant", "input", "Tracking your order...")
            write_message("assistant", "text", f"Your order status for {st.session_state.user_input} is:\n\n - In Transit\n - Estimated Delivery: 3 days")
    elif st.session_state.last_button == "Cancel Order":
        if st.session_state.user_input == "":
            write_message("user", "text", "I want to cancel my order.")
            write_message("assistant", "input", "Please enter your order ID to cancel your order.")
        elif st.session_state.user_input:
            write_message("user", "text", f"My order ID: {st.session_state.user_input}")
            write_message("assistant", "input", "Processing your cancellation request...")
            write_message("assistant", "text", f"Your order with ID {st.session_state.user_input} has been submitted for cancellation. You will receive a confirmation soon.")


def init():
    if "rule_based_messages" not in st.session_state:
        st.session_state.rule_based_messages = [
            {
                "role": "assistant",
                "type": "text",
                "content": "How may I assist you today?"
            },
            {
                "role": "assistant",
                "type": "button",
                "content": "Account Issues"
            },
            {
                "role": "assistant",
                "type": "button",
                "content": "Order Status"
            },
            {
                "role": "assistant",
                "type": "button",
                "content": "Talk to a Human Agent"
            }
        ]

        st.session_state.last_button = None
        st.session_state.user_input = ""

    messages = st.session_state.get("rule_based_messages", [])
    i = 0
    while i < len(messages):
        current_role = messages[i]["role"]
        group = []

        while i < len(messages) and messages[i]["role"] == current_role:
            group.append(messages[i])
            i += 1
        
        with st.chat_message(current_role):
            for msg in group:
                if msg["type"] == "button":
                    if st.button(msg["content"]):
                        st.session_state.last_button = msg["content"]
                else:
                    st.write(msg["content"])

def write_message(role, type, content):

    message = {
        "role": role,
        "type": type,
        "content": content
    }

    with st.chat_message(role):
        if type == "button":
            if st.button(content):
                st.session_state.last_button = content
        elif type == "input":
            if st.session_state.user_input == "":
                st.session_state.user_input = st.text_input(content)
                if st.session_state.user_input:
                    st.rerun()
            elif content == "Tracking your order...":
                st.write(f"Tracking your order with ID {st.session_state.user_input}...")
            elif content == "Processing your cancellation request...":
                st.write(f"Processing cancellation for order ID {st.session_state.user_input}...")
        else:
            st.write(content)

    st.session_state.rule_based_messages.append(message)

header()
main()