# InPoDa – Semantic Search on Legal Documents

## Context

This project was initially developed about two years ago as part of an academic assignment in data processing.  
It has recently been reviewed and slightly refactored to improve code readability, file naming consistency, and overall project structure.

The goal was to implement a simple semantic search system on a text corpus (legal articles), using embeddings and cosine similarity.

---

## Project Objective

The program allows to:

- Load a corpus of documents (one document per line in a .txt file)
- Transform each document into a numerical vector (embedding)
- Transform a user query into a vector
- Compute cosine similarity between the query and each document
- Display the most relevant documents

It is a small semantic search engine based on vector representations.

---

## How It Works

1. Documents are loaded from a text file (or a default corpus).
2. The SentenceTransformer model generates an embedding for each document.
3. The user enters a query.
4. Cosine similarity is computed between the query and each document.
5. Documents are sorted by descending similarity score.
6. The 3 most relevant documents are displayed.

Embeddings are also saved in a file named corpus_embeddings.json.

---

## Technologies Used

- Python  
- SentenceTransformers (paraphrase-MiniLM-L6-v2)  
- NumPy  
- JSON  

---

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt

Execution:
Run the program

python semantic_search.py

Then:
- Enter the name of the .txt file containing the corpus or type None to use the default corpus
- Enter the query to search for

```

## Project Structure

InPoDa/
│

├── semantic_search.py

├── legal_corpus.txt

├── corpus_embeddings.json

├── requirements.txt

└── README.md

## This project demonstrates:
- the use of embeddings for semantic search
- the transformation of text into vector representations
- the computation of cosine similarity
- a first applied approach to NLP
