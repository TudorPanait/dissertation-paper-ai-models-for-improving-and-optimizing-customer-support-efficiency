import os
from dotenv import load_dotenv

import streamlit as st
from textblob import TextBlob

from langchain_openai import ChatOpenAI

def header():
    st.set_page_config(page_title="Sentiment Analysis", page_icon=":bar_chart:")
    st.title("Sentiment Analysis")
    st.write("This page is dedicated to sentiment analysis tasks.")
    load_dotenv()

def main():
    st.subheader("Analyze the sentiment of your text")
    user_input = st.text_area("Enter text for sentiment analysis:", value="I don't know what to write here, but I want to analyze the sentiment of this text.")
    user_choice = st.selectbox("Choose analysis method:", ["TextBlob", "OpenAI"])

    if st.button("Analyze"):
        if user_input:
            if user_choice == "TextBlob":
                textblob_sentiment_analysis(user_input)
            else:
                st.write_stream(openai_sentiment_analysis(user_input))
        else:
            st.warning("Please enter some text to analyze.")

def textblob_sentiment_analysis(user_input):
    analysis = TextBlob(user_input)
    sentiment = analysis.sentiment
    st.write(f"Polarity: {sentiment.polarity}\n\n Subjectivity: {sentiment.subjectivity}")

def openai_sentiment_analysis(user_input):
    llm = ChatOpenAI(model="gpt-4.1-nano")
    for chunk in llm.stream(
        [
            (
                "system", 
                "You are a sentiment analysis assistant. Your purpose is to analyse the appended text for sentiment, polarity, subjectivity and to explain the reasoning behind your output. The output should follow the parttern - Sentiment (Negative/Neutral/Positive)\nPolarity(-1.0,1.0)\nSubjectivity(Low/Medium/High)\nExplanation"),
            (
                "human", 
                user_input
            )
        ]
    ):
        yield chunk.content

header()
main()