"""
=========================================================
Retriever Configuration
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Central configuration for the Retriever module.

Responsibilities
----------------
1. Qdrant collection settings
2. Search parameters
3. Embedding model settings
4. Retrieval thresholds

=========================================================
"""

# =====================================================
# Qdrant Configuration
# =====================================================

COLLECTION_NAME = "news_embeddings"

# =====================================================
# Retrieval Configuration
# =====================================================

TOP_K = 30

MAX_RESULTS = 20

SCORE_THRESHOLD = 0.65

# =====================================================
# Embedding Model
# =====================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

EMBEDDING_DIMENSION = 384

# =====================================================
# Search Configuration
# =====================================================

USE_METADATA_FILTER = True

RETURN_PAYLOAD = True

RETURN_VECTOR = False

# =====================================================
# Default Filters
# =====================================================

DEFAULT_TOPIC = None

DEFAULT_SENTIMENT = None

DEFAULT_NEWS_TYPE = None

DEFAULT_SOURCE = None

DEFAULT_START_DATE = None

DEFAULT_END_DATE = None

# =====================================================
# Logging
# =====================================================

LOG_LEVEL = "INFO"


