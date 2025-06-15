import os
from dotenv import load_dotenv

import streamlit as st

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

def header():
    st.set_page_config(page_title="Knowledge Management with Search", page_icon=":mag:")
    st.title("Knowledge Management with Search")
    load_dotenv()

    st.write("This page is dedicated to knowledge management and search functionality.")
    st.write("It uses the articles present in the `resources/articles` directory.")
    st.write("If searching with embeddings, it will search through the vector store in `resources/vectorstore`.")

def main():
    st.subheader("Search for Information")
    st.write("This feature allows you to search for information within a knowledge base.")
    use_embeddings = st.selectbox(
        "Select the method for search:",
        ["Use Keywords", "Use Embeddings"]
    )
    
    search_query = st.text_input("Enter your search query:")
    
    if search_query:
        if use_embeddings == "Use Keywords":
            search_with_keywords(search_query)
        else:
            search_with_embeddings(search_query)
        
def highlight_keywords(content, query):
    highlighted_content = content.replace(query, f" ***`{query}`*** " )
    return highlighted_content

def search_with_keywords(query):
    with st.spinner("Searching the knowledge base..."):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        articles_dir = os.path.join(script_dir, "..", "..", "resources", "articles")
        results = []
        
        for file in os.listdir(articles_dir):
            if file.endswith(".txt"):
                with open(os.path.join(articles_dir, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        highlighted_content = highlight_keywords(content, query)
                        results.append(Document(page_content=highlighted_content, metadata={"source": file}))
        
        if results:
            st.write("**Search Results:**")
            for result in results:
                st.write(f"**Source:** {result.metadata['source']}")
                st.write(result.page_content)
                st.write("---")
        else:
            st.warning("No results found for your query.")

def search_with_embeddings(query):
    with st.spinner("Searching the vector store..."):
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        db = FAISS.load_local("resources/vectorstore", embedding_model, allow_dangerous_deserialization=True)
        results = db.similarity_search(query, k=3)

        if results:
            st.write("**Search Results:**")
            for result in results:
                st.write(f"**Source:** {result.metadata['source']}")
                st.write(result.page_content)
                st.write("---")
        else:
            st.warning("No results found for your query.")

header()
main()