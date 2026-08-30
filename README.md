# 🤖 Agentic RAG Knowledge Assistant

An AI-powered **Agentic Retrieval-Augmented Generation (RAG) Assistant** built using **n8n and Google Gemini**. The system ingests knowledge from documents and URLs, converts the content into vector embeddings, stores it in a knowledge base, and enables an AI agent to retrieve relevant information and generate context-aware responses.

## 🚀 Features

- 🤖 Agentic RAG architecture
- 🧠 Google Gemini for LLM and embeddings
- 📚 Vector-based knowledge base
- 📄 Document ingestion
- 🌐 URL/web content ingestion
- 🔎 Semantic search and retrieval
- 💬 Conversational memory
- ⚙️ Automated workflows using n8n
- 🧩 Modular and extensible architecture

## 🏗️ Architecture

The project consists of two interconnected workflows:

### 1. Knowledge Base Ingestion

The ingestion workflow processes external knowledge and stores it in the vector database.

**Document Flow:**

`Document → Document Loader → Recursive Text Splitter → Gemini Embeddings → Vector Store → knowledge_base`

**URL Flow:**

`URL → URL Loader → Text Splitter → Gemini Embeddings → Vector Store → knowledge_base`

Both pipelines populate the centralized `knowledge_base`, allowing the AI assistant to retrieve information from multiple sources.

### 2. Agentic RAG Assistant

The conversational workflow allows users to interact with the AI agent.

`User Query → Chat Trigger → AI Agent → Knowledge Base Retrieval → Relevant Context → Gemini → Response`

The AI agent is connected to:

- **Google Gemini Chat Model**
- **Conversation Memory**
- **Knowledge Base Retrieval Tool**

This enables the assistant to retrieve relevant information from the knowledge base before generating responses.

## 🔍 How RAG Works

The system follows a Retrieval-Augmented Generation approach:

1. User submits a question.
2. The AI agent analyzes the query.
3. Relevant information is retrieved from the vector database.
4. Retrieved context is provided to the Gemini model.
5. Gemini generates a knowledge-grounded response.

This allows the assistant to answer questions using information stored in the custom knowledge base rather than relying solely on the model's pretrained knowledge.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **n8n** | Workflow automation and AI orchestration |
| **Google Gemini** | Language model and embeddings |
| **Vector Database** | Knowledge storage and semantic retrieval |
| **RAG** | Retrieval-augmented response generation |
| **AI Agent** | Intelligent retrieval and response generation |
| **Embeddings** | Semantic representation of knowledge |
| **Conversation Memory** | Multi-turn conversational context |

## 📂 Knowledge Sources

The current architecture supports ingestion from:

- Documents
- URLs / Web content

The architecture can be extended to support additional formats such as:

- PDF
- DOCX
- XLSX
- CSV
- TXT
- Other structured and unstructured data

## 🎯 Use Cases

- Company knowledge assistants
- Document Q&A systems
- Internal knowledge management
- Research assistants
- Educational assistants
- Technical documentation assistants
- Website knowledge assistants
- Enterprise information retrieval

## 📈 Future Enhancements

- Support for additional document formats
- Metadata-based filtering
- Hybrid search
- Retrieval reranking
- Query rewriting
- Source citations
- Duplicate document detection
- Automated knowledge-base updates
- Retrieval evaluation
- Hallucination detection
- Advanced chunking strategies
- Response quality benchmarking

## 🔐 Security

API keys and credentials should **never be committed to GitHub**.

Use n8n credentials or environment variables to securely manage API keys and other sensitive configuration.

## 📌 Project Highlights

- Built a complete **Agentic RAG pipeline** using n8n and Google Gemini.
- Developed separate **knowledge ingestion and conversational retrieval workflows**.
- Implemented **semantic retrieval using vector embeddings**.
- Integrated **conversation memory** for multi-turn interactions.
- Designed a modular architecture that can be extended to multiple knowledge sources and document formats.

## 👨‍💻 Project

**Agentic RAG Knowledge Assistant**

**Built with:** `n8n` · `Google Gemini` · `Vector Database` · `RAG` · `AI Agents`

> An intelligent knowledge assistant that ingests external information, retrieves relevant context, and generates conversational, knowledge-grounded responses.
