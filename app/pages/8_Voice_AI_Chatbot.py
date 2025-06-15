import os
from dotenv import load_dotenv

import streamlit as st
import tempfile
from openai import OpenAI

def header():
    st.set_page_config(page_title="Voice AI Chatbot", page_icon=":microphone:")
    st.title("Voice AI Chatbot")
    st.write("This page is dedicated to the voice AI agent that has no memory or tool access.")
    load_dotenv()

def main():
    st.subheader("Interact with the Voice AI Chatbot")
    client = OpenAI()

    audio = st.audio_input("Record a voice message")
    response = None
    text_response = None

    if audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_user_audio:
            tmp_user_audio.write(audio.getvalue())
            user_audio_path = tmp_user_audio.name

        with st.spinner("Processing your voice input..."):
            response = client.audio.transcriptions.create(
                file=open(user_audio_path, "rb"),
                model="gpt-4o-mini-transcribe",
                response_format="text"
            )

        st.info(response)
        st.write("---")

        with st.spinner("Generating response..."):
            text_response = client.responses.create(
                model="gpt-4.1-nano",
                input="Answer the following question from the user: " + str(response)
            ).output_text

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_assistant_audio:
                assistant_audio_path = tmp_assistant_audio.name
                with client.audio.speech.with_streaming_response.create(
                    model="gpt-4o-mini-tts",
                    voice="coral",
                    input=str(text_response),
                    instructions="Use a tone that resembles the sentiment of the text.",
                ) as audio_response:
                    audio_response.stream_to_file(assistant_audio_path)

            st.audio(assistant_audio_path, autoplay=True)
            st.success(text_response)

def init():
    if "voice_ai_messages" not in st.session_state:
        st.session_state.voice_ai_messages = [
            ("intstructions", AI_PROMPT),
            ("assistant", "Hello! I am Tudor, your virtual AI assistant for ABC Store. How may I assist you today?"),
        ]

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.voice_ai_messages.append(("user", user_input))
        knowledge_base_info = search_with_embeddings(user_input)

        llm = ChatOpenAI(model="gpt-4.1-nano")
        query = "History of the chat: " + str(st.session_state.voice_ai_messages) + "\nUser's latest request: " + user_input + "Information from our knowledge base: " + str(knowledge_base_info)
        
        response = llm.invoke(query) 
        
        st.session_state.voice_ai_messages.append(("assistant", response.content))

    for role, message in st.session_state.voice_ai_messages:
        if role == "user":
            st.chat_message("user").write(message)
        elif role == "assistant":
            st.chat_message("assistant").write(message)


header()
main()