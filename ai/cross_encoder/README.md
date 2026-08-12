# Cross Encoder

## Purpose

The Cross Encoder reranks the documents retrieved from Qdrant.

Instead of relying only on vector similarity, it compares the complete query with every retrieved document and assigns a semantic relevance score.

---

## Workflow

User Query

↓

Retriever (Top 10)

↓

Cross Encoder

↓

Top 5 Documents

↓

Context Builder

↓

LLM

---

## Model

cross-encoder/ms-marco-MiniLM-L-6-v2

---

## Files

config.py

model.py

reranker.py

formatter.py

logger.py

exceptions.py

test_reranker.py

---

## Run

```bash
python -m ai.cross_encoder.test_reranker
```