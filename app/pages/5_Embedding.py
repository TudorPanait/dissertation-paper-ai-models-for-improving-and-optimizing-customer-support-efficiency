import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import faiss
import pickle
from sklearn.manifold import TSNE
import plotly.express as px

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


def header():
    st.set_page_config(page_title="Embedding", page_icon=":link:")
    st.title("Embedding")
    st.write("This page is dedicated to the embedding functionality.")
    load_dotenv()

def main():
    st.subheader("Create Embeddings from Text Files")
    st.write("This functionality allows you to create embeddings from text files stored in the `resources/articles`.")
    
    st.write("**These are the texts that will be used to create embeddings:**")
    for file in os.listdir("resources/articles"):
        if file.endswith(".txt"):
            with st.expander(file):
                with open(os.path.join("resources/articles", file), "r", encoding="utf-8") as f:
                    content = f.read()
                    st.write(content)

    if st.button("Create Embeddings"):
        docs = []
        script_dir = os.path.dirname(os.path.abspath(__file__))
        articles_dir = os.path.join(script_dir, "..", "..", "resources", "articles")

        for file in os.listdir(articles_dir):
            if file.endswith(".txt"):
                with open(os.path.join("resources/articles", file), "r", encoding="utf-8") as f:
                    content = f.read()
                    docs.append(Document(page_content=content, metadata={"source": file}))
        
        chunks = chunk_documents(docs)
        create_embeddings(chunks)

    
def chunk_documents(docs, chunk_size=500, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_documents(docs)

def create_embeddings(chunks):
    with st.spinner("Creating embeddings..."):
        if chunks:
            embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
            db = FAISS.from_documents(chunks, embedding_model)
            db.save_local("resources/vectorstore")

            st.balloons()
            st.success("Embeddings created and saved successfully in the `resources/vectorstore` directory! Use them for search functionality available in the next page.")

            chunk_data = [{"Source": chunk.metadata["source"], "Chunk Size": len(chunk.page_content)} for chunk in chunks]
            df = pd.DataFrame(chunk_data)
            chunk_counts = df.groupby("Source").size().reset_index(name="Chunks")
            st.write("**Number of Chunks per Document:**")
            st.bar_chart(chunk_counts.set_index("Source"))

            visualize_embeddings("resources/vectorstore/index.faiss", "resources/vectorstore/index.pkl")
        else:
            st.error("No documents found to create embeddings. Please upload a text file or ensure the sample texts are available.")

def visualize_embeddings(faiss_path, meta_path):
    if os.path.exists(faiss_path) and os.path.exists(meta_path):
        index = faiss.read_index(faiss_path)
        with open(meta_path, 'rb') as f:
            metadata = pickle.load(f)
    else:
        st.error("❌ FAISS index or metadata not found.")
        return

    num_vectors = index.ntotal
    vectors = index.reconstruct_n(0, num_vectors)
    reduced_vectors = TSNE(n_components=3, random_state=42).fit_transform(vectors)

    if isinstance(metadata, list):
        labels = [m.get('text', f"Chunk {i}") if isinstance(m, dict) else str(m) for i, m in enumerate(metadata)]
    else:
        labels = [f"Chunk {i}" for i in range(num_vectors)]

    fig = px.scatter_3d(
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
        z=reduced_vectors[:, 2],
        hover_name=labels,
        title="FAISS 3D Embedding Visualization"
    )
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)

header()
main()