import os
from dotenv import load_dotenv

import streamlit as st

from langchain_openai import ChatOpenAI

def header():
    st.set_page_config(page_title="Intent Analysis", page_icon=":left_right_arrow:")
    st.title("Intent Analysis")
    st.write("This page is dedicated to intent analysis tasks.")
    load_dotenv()

def main():
    st.subheader("Analyze the intent of your text")
    user_input = st.text_area("Enter text for intent analysis:", value="I don't know what to write here, but I want to analyze the intent of this text.")
    
    if st.button("Analyze"):
        if user_input:
            st.write_stream(openai_intent_analysis(user_input))
        else:
            st.warning("Please enter some text to analyze.")

def openai_intent_analysis(user_input):
    llm = ChatOpenAI(model="gpt-4.1-nano")

    for chunk in llm.stream(
        [
            (
                "system", 
                "You are an intent analysis assistant. Your purpose is to analyse the appended text for intent, and to explain the reasoning behind your output. The output should follow the pattern - Intent (Action/Information/Question)\nExplanation"
            ),
            (
                "human", 
                user_input
            )
        ]
    ):
        yield chunk.content


header()
main()