# 📄 Document Research & Theme Identification Chatbot

An AI-powered web application that allows users to upload multiple documents (PDFs or images), extracts text using OCR, identifies common themes across all documents using clustering, and answers user questions with cited references — all through an interactive chatbot interface.

---

## 🚀 Project Idea

The goal of this project is to simulate a document researcher powered by AI. It:

- Extracts text from a large number of PDFs or scanned images.
- Breaks the content into small chunks for analysis.
- Identifies themes across documents using clustering (KMeans).
- Enables semantic search and intelligent Q&A using embeddings and vector search (FAISS).
- Provides an easy-to-use interface via Streamlit.

Use cases include:
- Legal document summarization
- Research paper exploration
- Policy analysis
- Business contract insights

---

## 🧠 Core Features

- 📄 Multi-format document upload (PDF, JPG, PNG, etc.)
- 🧹 Text extraction and cleaning using OCR and parsing
- ✂️ Text chunking for better analysis
- 🧵 Theme identification using unsupervised clustering (KMeans)
- 💬 Natural language Q&A powered by sentence embeddings and vector search
- 🔍 Citation-aware answers with high relevance

---

## 🛠️ Tech Stack

| Technology        | Purpose                                                                 |
|-------------------|-------------------------------------------------------------------------|
| **Python**        | Main programming language                                                |
| **Streamlit**     | Frontend web app framework for fast prototyping                          |
| **Tesseract OCR** | Extracts text from image-based scanned documents                         |
| **PyMuPDF (fitz)**| Extracts text from PDFs                                                   |
| **scikit-learn**  | KMeans clustering for theme detection                                     |
| **FAISS**         | Fast Approximate Nearest Neighbor search for semantic retrieval          |
| **SentenceTransformers** | Converts text into embeddings for similarity search (MiniLM model)     |

---

## 🧩 Why These Technologies?

### 1. **Streamlit**
- Rapid UI development for ML apps
- Lightweight and requires minimal frontend code

### 2. **Tesseract OCR**
- Open-source and efficient for extracting text from scanned documents

### 3. **SentenceTransformers (MiniLM)**
- Pre-trained LLM-based embeddings for capturing sentence meaning
- Lightweight (`all-MiniLM-L6-v2`) yet powerful for semantic tasks

### 4. **FAISS**
- Super fast and accurate for similarity search in large embedding spaces

### 5. **KMeans Clustering**
- Simple, effective unsupervised method for grouping related text chunks into themes

---

📧 Email: dakshitaarora04@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/dakshitaarora04

