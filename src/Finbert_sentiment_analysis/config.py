# """
# config.py
# Application configuration
# """

# # -----------------------------
# # Database
# # -----------------------------

# DB_HOST = "localhost"
# DB_PORT = 3306
# DB_USER = "root"
# DB_PASSWORD = "your_password"
# DB_NAME = "stock_market_analytics"

# # -----------------------------
# # ETL
# # -----------------------------

# BATCH_SIZE = 100

# COMMIT_INTERVAL = 100

# MAX_TEXT_LENGTH = 512

# # -----------------------------
# # FinBERT
# # -----------------------------

# MODEL_NAME = "ProsusAI/finbert"

# # -----------------------------
# # Logging
# # -----------------------------

# LOG_DIR = "logs"

# LOG_FILE = "logs/sentiment_etl.log"


"""
==========================================================
Configuration File

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System
==========================================================
"""

# ==========================================================
# Database Configuration
# ==========================================================

DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "@MariaDB123"
DB_NAME = "stock_market_analytics"

# ==========================================================
# ETL Configuration
# ==========================================================

BATCH_SIZE = 100
COMMIT_INTERVAL = 100
MAX_TEXT_LENGTH = 512

# ==========================================================
# FinBERT Configuration
# ==========================================================

MODEL_NAME = "ProsusAI/finbert"

# ==========================================================
# Logging Configuration
# ==========================================================

LOG_DIR = "logs"
LOG_FILE = "logs/sentiment_etl.log"