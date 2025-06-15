import os
from dotenv import load_dotenv

import streamlit as st

from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain.callbacks.streamlit import StreamlitCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import tool

@tool
def search_knowledge_base(query: str) -> list:
    """
    Search the internal knowledge base when in need of more information about products, services, or general inquiries.
    Search one word at a time, or multiple terms separated by commas.
    Searching the same word will return the same results.

    Args:
        query (str): The user's query to search for relevant information.

    Returns:
        list: A list of relevant documents from the knowledge base.
    """
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

    if "," in query:
        items = [item.strip() for item in query.split(",")]
    elif " " in query:
        items = [item.strip() for item in query.split(" ")]
    else:
        items = [query]

    results = []

    for item in items:
        db = FAISS.load_local("resources/vectorstore", embedding_model, allow_dangerous_deserialization=True)
        results.append(db.similarity_search(item, k=3))
    
    return results

PROMPT = PromptTemplate.from_template("""
                                    You are Tudor, an intelligent and friendly AI assistant for a fictional online electronics retailer called ABC Store.
                                    Answer the following questions.
                                    
                                    You have access to the following tools:

                                    {tools}

                                    Use the following format:

                                    Question: the input question or questions you must answer; always split the input into multiple questions if it contains multiple questions
                                    Thought: your reasoning
                                    Action: the action to take, should be one of [{tool_names}]
                                    Action Input: the input to the action
                                    Observation: the result of the action
                                    ... (this Thought/Action/Action Input/Observation can repeat a maximum of 3 times in order to answer the question or questions; after the 3rd time answer the question and skip the Action/Action Input/Observation steps and go straight to the Final Answer)
                                    Thought: I now know enough to answer the question
                                    Final Answer: the final output formatted nicely and clearly using markdown
                                    
                                    Start by thinking about the input question or questions, then use the tools to gather information if needed, and finally provide a comprehensive answer in a timely manner.

                                    Question: {input}
                                    {agent_scratchpad}
                                    """)

def header():
    st.set_page_config(page_title="ReACT & MRKL", page_icon=":robot:")
    st.title("ReACT & MRKL")
    st.write("This page demonstrates the ReACT (Reasoning and Acting) and MRKL (Modular Reasoning and Knowledge Learning) agent capabilities.")
    load_dotenv()

def main():
    st.subheader("Interact with the ReACT & MRKL agent")
    init()

def init():
    llm = ChatOpenAI(model="gpt-4.1-mini", streaming=True)
    tools = [search_knowledge_base]
    agent = create_react_agent(llm, tools, PROMPT)
    agent_executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)

    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent_executor.invoke(
                {"input": prompt}, {"callbacks": [st_callback]}
            )

            st.write(response["output"])

header()
main()

