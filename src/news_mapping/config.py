"""
==============================================================================
News Mapping Configuration
==============================================================================

Project : AI-Driven Stock Market Intelligence System

Description
-----------
Configuration values used by the News Mapping ETL.

==============================================================================
"""

# -----------------------------------------------------------------------------
# ETL Configuration
# -----------------------------------------------------------------------------

# Number of news articles after which progress is logged
LOG_PROGRESS_EVERY = 500

# Number of rows inserted in one batch
BATCH_SIZE = 1000

# Default relevance score assigned to every mapping
DEFAULT_RELEVANCE_SCORE = 1.00


# -----------------------------------------------------------------------------
# Company Matching Configuration
# -----------------------------------------------------------------------------

# Minimum alias length to consider
MIN_ALIAS_LENGTH = 3

# Remove ".NS" suffix from stock symbols
REMOVE_NS_SUFFIX = True

# Enable stock symbol matching
MATCH_SYMBOL = True

# Enable company name matching
MATCH_COMPANY_NAME = True

# Enable alias matching
MATCH_ALIAS = True


# -----------------------------------------------------------------------------
# Future Features
# -----------------------------------------------------------------------------

# Use fuzzy matching (RapidFuzz)
ENABLE_FUZZY_MATCH = False

# Fuzzy match threshold
FUZZY_MATCH_THRESHOLD = 90

# Enable Named Entity Recognition (spaCy)
ENABLE_NER = False

# Minimum confidence for AI/NER-based matching
NER_CONFIDENCE = 0.80