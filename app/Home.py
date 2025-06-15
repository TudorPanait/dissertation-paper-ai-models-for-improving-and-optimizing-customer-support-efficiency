import streamlit as st

def header():
    st.set_page_config(page_title="Home", page_icon=":house:")
    st.title("AI Models for Improving and Optimizing Customer Support Efficiency")
    st.write("This application leverages AI models to showcase how companies can improve and optimize customer support efficiency.")

def main():
    st.header("📌 Purpose of the Application")
    st.write("""
        Welcome to the practical chapter of this dissertation, **Hands-On AI with Prototypes and Practical Applications**. 
        \nHere, the focus shifts from theory to real-world implementation, exploring how AI technologies can be leveraged to enhance customer support efficiency. 
        \nThis section provides an overview of available tools, APIs, SDKs, and frameworks—both commercial and open-source—that empower organizations of all sizes to optimize their customer support processes. 
        \nThrough practical examples and prototypes, you will discover actionable ways to integrate AI into customer service workflows and drive meaningful improvements.
    """)

    st.header("🛠️ Demos Available")
    st.write("Here are the demos and applications integrated into this project and their functionalities:")

    st.subheader("1. Sentiment Analysis")
    st.write("""
        - **Purpose**: Analyze the sentiment of customer messages to better understand customer emotions and improve support responses.
        - **How to Use**: Navigate to the Sentiment Analysis page, input or upload customer messages, and view the sentiment results (positive, negative, or neutral).
    """)

    st.subheader("2. Intent Analysis")
    st.write("""
        - **Purpose**: Detect the underlying intent behind customer messages to route and prioritize support requests efficiently.
        - **How to Use**: Go to the Intent Analysis page, input or upload customer queries, and view the detected intent categories.
    """)
    
    st.subheader("3. Rule-Based System")
    st.write("""
        - **Purpose**: Demonstrate traditional rule-based approaches for handling customer support queries.
        - **How to Use**: Visit the Rule-Based System page, input customer messages, and observe how predefined rules classify or respond to queries.
    """)

    st.subheader("4. Keyword-Based Classification")
    st.write("""
        - **Purpose**: Classify customer messages based on the presence of specific keywords to quickly identify topics or issues.
        - **How to Use**: Go to the Keyword-Based Classification page, input or upload customer messages, and see which keywords or categories are detected.
    """)

    st.subheader("5. Embedding")
    st.write("""
        - **Purpose**: Create embeddings from text files for semantic search and similarity analysis.
        - **How to Use**: Upload text files or use preloaded ones to generate embeddings and visualize them in a 3D space.
    """)

    st.subheader("6. Knowledge Management with Search")
    st.write("""
        - **Purpose**: Manage and search through a knowledge base of articles to provide quick answers to customer queries.
        - **How to Use**: Navigate to the Knowledge Management page, input search queries, and view relevant articles or documents.
    """)

    st.subheader("7. Conversational AI Chatbot")
    st.write("""
        - **Purpose**: Engage with a conversational AI chatbot that can remember past interactions and access tools for enhanced support.
        - **How to Use**: Visit the Conversational AI Chatbot page, chat with the AI, and see how it utilizes memory and tools to assist you.
    """)

    st.subheader("8. Voice AI Chatbot")
    st.write("""
        - **Purpose**: Interact with a voice AI chatbot that can transcribe audio input and respond with synthesized speech.
        - **How to Use**: Go to the Voice AI Chatbot page, record your voice message, and listen to the AI's response.
    """)

    st.subheader("9. Rule-Based Chatbot")
    st.write("""
        - **Purpose**: Demonstrate a rule-based chatbot that follows predefined rules to assist customers with common issues.
        - **How to Use**: Visit the Rule-Based Chatbot page, select options based on your issue, and see how the bot guides you through the process.
    """)

    st.subheader("10. React & MRKL Agent")
    st.write("""
        - **Purpose**: Demonstrate a React-style agent using the MRKL (Modular Reasoning, Knowledge, and Language) paradigm to combine multiple tools and reasoning steps for complex customer support tasks.
        - **How to Use**: Go to the React & MRKL Agent page, input your query, and observe how the agent decomposes the problem, uses different tools, and provides a comprehensive answer.
    """)

    st.header("📖 How to Use the Application")
    st.write("""
        1. Use the sidebar to navigate between pages.
        2. Follow the instructions provided on each page to interact with the tools.
        3. Explore the functionalities and visualize the results to understand how AI can optimize customer support workflows.
    """)

    st.header("🚀 Getting Started")
    st.write("""
        1. Clone the repository.
        2. Create and activate the virtual environment:
           ```
           python -m venv .venv-win
           .venv-win\\Scripts\\activate
           ```
        3. Install dependencies:
           ```
           pip install -r requirements.txt
           ```
        4. Add your environment variables to `.env`.
        5. Run the Streamlit app:
           ```
           streamlit run your_app.py
           ```
    """)

    st.header("📜 License")
    st.write("""
        See [LICENSE](https://github.com/TudorPanait/dissertation-paper-ai-models-for-improving-and-optimizing-customer-support-efficiency/blob/main/LICENSE) for details.
    """)

header()
main()