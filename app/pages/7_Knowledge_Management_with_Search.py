import streamlit as st

def header():
    st.set_page_config(page_title="Knowledge Management with Search", page_icon=":mag:")
    st.title("Knowledge Management with Search")
    st.write("This page is dedicated to knowledge management and search functionality.")
    st.warning("🚧 This feature is a Work In Progress (WIP).", icon="⚠️")

header()