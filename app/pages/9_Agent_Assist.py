import streamlit as st

def header():
    st.set_page_config(page_title="Agent Assist", page_icon="🤖")
    st.title("Agent Assist")
    st.write("This page is dedicated to the Agent Assist feature for customer support.")
    st.warning("🚧 This feature is a Work In Progress (WIP).", icon="⚠️")

header()