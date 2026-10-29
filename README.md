# RAG Knowledge Hub

Retrieval-augmented generation starter for document ingestion, embeddings, and grounded Q&A.

Build a private knowledge assistant that answers from *your* docs instead of model memory alone.

## Features

- Chunk and embed PDFs, Markdown, and plain text
- Vector store abstraction (local starter included)
- Citation-friendly answers with retrieved context
- Simple CLI ask loop for local testing

## Project layout

```text
src/
  ingest.py      # load + chunk + embed documents
  retrieve.py    # similarity search
  answer.py      # grounded generation
  store/         # local vector store helpers
data/            # drop sample docs here
requirements.txt
```

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# ingest
python -m src.ingest --input data/

# ask
python -m src.answer --query "What does this project cover?"
```

## Typical pipeline

```text
Documents → Chunking → Embeddings → Vector index → Retrieve → Generate + cite
```

## Good next steps

- Swap the local store for Pinecone / Qdrant / pgvector
- Add hybrid search (keyword + vector)
- Add evals for faithfulness and citation coverage

## License

MIT
