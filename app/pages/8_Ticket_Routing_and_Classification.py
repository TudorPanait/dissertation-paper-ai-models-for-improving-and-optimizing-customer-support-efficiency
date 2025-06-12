import streamlit as st

def header():
    st.set_page_config(page_title="Ticket Routing & Classification", page_icon=":ticket:")
    st.title("Ticket Routing & Classification")
    st.write("This page is dedicated to ticket routing and classification using AI models.")
    st.warning("🚧 This feature is a Work In Progress (WIP).", icon="⚠️")

header()