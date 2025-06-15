# AI Models for Improving and Optimizing Customer Support Efficiency

Welcome to the practical chapter of this dissertation, **Hands-On AI with Prototypes and Practical Applications**. Here, the focus shifts from theory to real-world implementation, exploring how AI technologies can be leveraged to enhance customer support efficiency. This section provides an overview of available tools, APIs, SDKs, and frameworks—both commercial and open-source—that empower organizations of all sizes to optimize their customer support processes. Through practical examples and prototypes, you will discover actionable ways to integrate AI into customer service workflows and drive meaningful improvements.

---

**Dissertation:** AI Models for Improving and Optimizing Customer Support Efficiency  
**Scientific coordinator:** Conf. Univ. Dr. BUȘU Mihail  
**Student:** PANAIT Tudor-Alexandru

---

## Purpose of the Application

This application leverages AI models to improve and optimize customer support efficiency. It provides demos and applications that showcase how AI technologies can enhance workflows, reduce response times, and improve customer satisfaction.

---

## Applications Available

### 1. Home
- **Purpose**: Introduces the project and its goals. Provides an overview of the applications and how they contribute to improving customer support efficiency.
- **How to Use**: Start here to understand the purpose of the project and navigate to other pages using the sidebar.

### 2. Sentiment Analysis
- **Purpose**: Analyze the sentiment of customer messages to better understand customer emotions and improve support responses.
- **How to Use**: Navigate to the Sentiment Analysis page, input or upload customer messages, and view the sentiment results (positive, negative, or neutral).

### 3. Intent Analysis
- **Purpose**: Detect the underlying intent behind customer messages to route and prioritize support requests efficiently.
- **How to Use**: Go to the Intent Analysis page, input or upload customer queries, and view the detected intent categories.

### 4. Rule-Based System
- **Purpose**: Demonstrate traditional rule-based approaches for handling customer support queries.
- **How to Use**: Visit the Rule-Based System page, input customer messages, and observe how predefined rules classify or respond to queries.

### 5. Keyword-Based Classification
- **Purpose**: Classify customer messages based on the presence of specific keywords to quickly identify topics or issues.
- **How to Use**: Go to the Keyword-Based Classification page, input or upload customer messages, and see which keywords or categories are detected.

### 6. Embedding
- **Purpose**: Create embeddings from text files for semantic search and similarity analysis.
- **How to Use**: Upload text files or use preloaded ones to generate embeddings and visualize them in a 3D space.

### 7. Knowledge Management with Search
- **Purpose**: Manage and search through a knowledge base of articles to provide quick answers to customer queries.
- **How to Use**: Navigate to the Knowledge Management page, input search queries, and view relevant articles or documents.

### 8. Conversational AI Chatbot
- **Purpose**: Engage with a conversational AI chatbot that can remember past interactions and access tools for enhanced support.
- **How to Use**: Visit the Conversational AI Chatbot page, chat with the AI, and see how it utilizes memory and tools to assist you.

### 9. Voice AI Chatbot
- **Purpose**: Interact with a voice AI chatbot that can transcribe audio input and respond with synthesized speech.
- **How to Use**: Go to the Voice AI Chatbot page, record your voice message, and listen to the AI's response.

### 10. Rule-Based Chatbot
- **Purpose**: Demonstrate a rule-based chatbot that follows predefined rules to assist customers with common issues.
- **How to Use**: Visit the Rule-Based Chatbot page, select options based on your issue, and see how the bot guides you through the process.

### 11. React & MRKL Agent
- **Purpose**: Demonstrate a React-style agent using the MRKL (Modular Reasoning, Knowledge, and Language) paradigm to combine multiple tools and reasoning steps for complex customer support tasks.
- **How to Use**: Go to the React & MRKL Agent page, input your query, and observe how the agent decomposes the problem, uses different tools, and provides a comprehensive answer.

---

## Folder Structure

```
├── app/                       # Streamlit pages
│   ├── pages/
├── resources/
│   ├── articles/              # Sample text files for embedding
│   ├── vectorstore/           # FAISS index and metadata
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # License file
```

## How to Use the Application

1. Use the sidebar to navigate between pages.
2. Follow the instructions provided on each page to interact with the tools.
3. Explore the functionalities and visualize the results to understand how AI can optimize customer support workflows.

---

## Getting Started

1. Clone the repository.
2. Create and activate the virtual environment:
   <details>
   <summary>Windows</summary>

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
   </details>

   <details>
   <summary>macOS / Linux</summary>

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   </details>
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your environment variables to `.env`.
5. Run the Streamlit app:
   ```bash
   streamlit run app/Home.py
   ```

---

## License

See [LICENSE](LICENSE) for details.