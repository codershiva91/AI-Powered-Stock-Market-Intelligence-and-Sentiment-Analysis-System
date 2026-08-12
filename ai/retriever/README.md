<!-- Why this configuration?

Variable	 Purpose
COLLECTION_NAME	      Qdrant collection to search
TOP_K	Default       number of documents returned
MAX_RESULTS	Upper     limit for retrieval
SCORE_THRESHOLD	      Minimum similarity score accepted
EMBEDDING_MODEL	      Same model used for indexing and querying
EMBEDDING_DIMENSION	  Must match your stored vectors (384)
RETURN_PAYLOAD	      Include article metadata in results
RETURN_VECTOR	       Disabled because the LLM doesn't need raw vectors

#Retriever Architecture

                   User Query
                        │
                        ▼
              Retriever.search()
                        │
                        ▼
          Sentence Transformer Model
             (Existing Module)
                        │
                        ▼
                Query Embedding
                        │
                        ▼
               Existing QdrantManager
                        │
                        ▼
               Semantic Vector Search
                        │
                        ▼
             Raw Qdrant Search Results
                        │
                        ▼
                 formatter.py
                        │
                        ▼
             Structured Search Results -->