<!-- Sprint 1: Semantic Search
Sprint Goal

Build a production-ready Semantic Search Engine that searches 40,203 news vectors stored in Qdrant.


Step 1: exceptions.py

This file will define custom exceptions for the Semantic Search module.

Instead of showing cryptic Python errors, we'll raise meaningful exceptions.


Step 2 (Next)

We'll implement formatter.py.

Its job is to convert raw Qdrant search results into a clean, readable format.

========================================================

Result #1

Similarity Score : 0.9241

Title            : Reliance Industries Q1 Results

Source           : Economic Times

Sentiment        : Positive

Published Date   : 2026-07-23

--------------------------------------------------------

Document

Reliance Industries reported stronger-than-expected...

========================================================


Sprint 1 Architecture

By the end of this sprint, the flow will be:

User Query
      │
      ▼
SemanticSearch.search()
      │
      ▼
Sentence Transformer
      │
      ▼
Qdrant Search
      │
      ▼
Formatter
      │
      ▼
Console Output


Next Step (Step 2)

We'll implement formatter.py.

Its responsibility will be:

Raw Qdrant Results
        │
        ▼
Formatter
        │
        ▼
Beautiful Console Output

Example:

========================================================

Result #1

Similarity Score : 0.9238

Title            : Reliance Industries reports Q1 earnings

Source           : Economic Times

Sentiment        : Positive

Published Date   : 2026-07-24

--------------------------------------------------------

Document

Reliance Industries reported stronger-than-expected
quarterly earnings driven by telecom and refining...

========================================================

Sprint 1 — Step 3

Responsibility

This module filters search results by:

✅ Sentiment
✅ Source
✅ Topic
✅ News Type
✅ Company/Symbol (future-ready)

Sprint 1 — Step 4
File

Responsibility

This class should only:

Validate the query
Generate the query embedding
Search Qdrant
Return standardized search results
Raise meaningful exceptions

 -->
