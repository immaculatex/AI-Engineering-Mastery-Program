# AI Document Reader & Text Chunker

This project is part of the **AI Engineering Mastery Program**.  
It demonstrates how real GenAI systems ingest and prepare documents before
sending them to embeddings, vector databases, or LLMs.

The pipeline reads **PDF and DOCX files**, cleans the extracted text, and
splits it into overlapping chunks suitable for **RAG (Retrieval-Augmented Generation)**.

## Features
- PDF parsing using pdfplumber
- DOCX parsing using python-docx
- Text cleaning & normalization
- LangChain recursive chunking
- Ready for embeddings and vector databases

## How to Run
python3 -m pip install pdfplumber python-docx langchain-text-splitters
python main.py
