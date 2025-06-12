import streamlit as st

def header():
    st.set_page_config(page_title="Voice AI Agent", page_icon=":microphone:")
    st.title("Voice AI Agent")
    st.write("This page is dedicated to the voice AI agent.")
    st.warning("🚧 This feature is a Work In Progress (WIP).", icon="⚠️")

header()