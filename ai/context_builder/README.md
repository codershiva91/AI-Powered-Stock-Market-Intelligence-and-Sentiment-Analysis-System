# Context Builder

## Purpose

The Context Builder converts reranked documents into a structured context that can be sent directly to an LLM.

---

## Pipeline

User Query

↓

Retriever

↓

Cross Encoder

↓

Context Builder

↓

Prompt Builder

↓

Gemini / OpenAI

---

## Output

DOCUMENT 1

Title

Source

Topic

Sentiment

Published

Content

-------------------------

DOCUMENT 2

...

---

## Run

```bash
python -m ai.context_builder.test_builder
```