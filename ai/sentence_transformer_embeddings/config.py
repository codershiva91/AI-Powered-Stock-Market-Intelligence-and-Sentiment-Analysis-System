"""
Configuration settings for the Sentence Transformer Embedding module.
"""

import os
import torch


# ==============================================================================
# MODEL CONFIGURATION
# ==============================================================================

# Sentence Transformer model
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Embedding dimension of the model
EMBEDDING_DIMENSION = 384

# Maximum sequence length accepted by the model
MAX_SEQUENCE_LENGTH = 256


# ==============================================================================
# DEVICE CONFIGURATION
# ==============================================================================

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Number of texts to encode in one batch
BATCH_SIZE = 32


# ==============================================================================
# DATABASE CONFIGURATION
# ==============================================================================

# DB_CONFIG = {
#     "host": "127.0.0.1",      # Prefer 127.0.0.1 over localhost
#     "port": 3306,
#     "user": "root",
#     "password": "@MariaDB123",
#     "database": "stock_market_analytics",
# }

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": os.getenv("DB_PASSWORD"),
    "database": "stock_market_analytics",
}

# ==============================================================================
# NEWS TABLE CONFIGURATION
# ==============================================================================

NEWS_TABLE = "news_articles"

PRIMARY_KEY = "news_id"

TEXT_COLUMN = "article_text"


# ==============================================================================
# QDRANT CONFIGURATION
# ==============================================================================

QDRANT_HOST = "localhost"

QDRANT_PORT = 6333

COLLECTION_NAME = "news_embeddings"


# ==============================================================================
# ETL CONFIGURATION
# ==============================================================================

# Number of records fetched from MariaDB at a time
FETCH_BATCH_SIZE = 500

# Number of vectors uploaded to Qdrant at once
UPLOAD_BATCH_SIZE = 100

# Resume from previous run
ENABLE_RESUME = True

# Print progress after every N records
PROGRESS_INTERVAL = 100


# ==============================================================================
# LOGGING CONFIGURATION
# ==============================================================================

LOG_DIRECTORY = "logs"

LOG_FILE = os.path.join(LOG_DIRECTORY, "embedding_etl.log")

LOG_LEVEL = "INFO"


# ==============================================================================
# EMBEDDING CONFIGURATION
# ==============================================================================

# Normalize embeddings before storing
NORMALIZE_EMBEDDINGS = True

# Convert embeddings to list before upload
CONVERT_TO_LIST = True


# ==============================================================================
# APPLICATION CONFIGURATION
# ==============================================================================

APPLICATION_NAME = "Sentence Transformer Embedding Pipeline"

VERSION = "1.0.0"