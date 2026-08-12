"""
==============================================================================
Query Analyzer Configuration
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Configuration settings for Query Analyzer V2
==============================================================================
"""

# ==============================================================================
# SUPPORTED INTENTS
# ==============================================================================

SUPPORTED_INTENTS = [

    "COMPARE_COMPANIES",

    "STOCK_SENTIMENT",

    "SECTOR_ANALYSIS",

    "MARKET_ANALYSIS",

    "LATEST_NEWS",

    "GENERAL_QUERY"

]

# ==============================================================================
# INTENT PRIORITY
# ==============================================================================

INTENT_PRIORITY = [

    "COMPARE_COMPANIES",

    "STOCK_SENTIMENT",

    "SECTOR_ANALYSIS",

    "MARKET_ANALYSIS",

    "LATEST_NEWS",

    "GENERAL_QUERY"

]

# ==============================================================================
# INTENT PATTERNS
# ==============================================================================

INTENT_PATTERNS = {

    "COMPARE_COMPANIES": [

        "compare",
        "comparison",
        "vs",
        "versus",
        "difference",
        "better",
        "better than",
        "which is better",
        "against",
        "compare with"

    ],

    "STOCK_SENTIMENT": [

        "positive",
        "negative",
        "bullish",
        "bearish",
        "sentiment",
        "opinion",
        "outlook"

    ],

    "SECTOR_ANALYSIS": [

        "sector",
        "banking",
        "bank",
        "it",
        "technology",
        "tech",
        "pharma",
        "healthcare",
        "energy",
        "fmcg",
        "metal",
        "auto",
        "automobile",
        "realty",
        "media",
        "chemical",
        "financial"

    ],

    "MARKET_ANALYSIS": [

        "market",
        "market trend",
        "market movement",
        "market analysis",
        "index",
        "nifty",
        "nifty 50",
        "bank nifty",
        "sensex"

    ],

    "LATEST_NEWS": [

        "news",
        "headline",
        "headlines",
        "latest",
        "recent",
        "update",
        "updates"

    ]

}

# ==============================================================================
# MARKET INDICES
# ==============================================================================

SUPPORTED_INDICES = [

    "BANK NIFTY",

    "NIFTY 50",

    "NIFTY",

    "SENSEX"

]

# ==============================================================================
# SUPPORTED SECTORS
# ==============================================================================

SUPPORTED_SECTORS = [

    "BANKING",

    "IT",

    "AUTO",

    "ENERGY",

    "FMCG",

    "PHARMA",

    "METAL",

    "REALTY",

    "MEDIA",

    "CHEMICAL",

    "FINANCIAL"

]

# ==============================================================================
# SUPPORTED SENTIMENTS
# ==============================================================================

SUPPORTED_SENTIMENTS = [

    "POSITIVE",

    "NEGATIVE",

    "NEUTRAL",

    "BULLISH",

    "BEARISH"

]

# ==============================================================================
# TIME FILTERS
# ==============================================================================

TIME_PATTERNS = {

    "TODAY": [

        "today"

    ],

    "YESTERDAY": [

        "yesterday"

    ],

    "LAST_7_DAYS": [

        "last 7 days",
        "last seven days"

    ],

    "LAST_WEEK": [

        "last week"

    ],

    "THIS_WEEK": [

        "this week"

    ],

    "LAST_MONTH": [

        "last month"

    ],

    "THIS_MONTH": [

        "this month"

    ],

    "THIS_YEAR": [

        "this year"

    ],

    "LAST_YEAR": [

        "last year"

    ]

}

# ==============================================================================
# DEFAULT VALUES
# ==============================================================================

DEFAULT_INTENT = "GENERAL_QUERY"

DEFAULT_CONFIDENCE = 0.0

DEFAULT_TIME_FILTER = None

DEFAULT_SENTIMENT = None

DEFAULT_SECTOR = None

DEFAULT_MARKET_INDEX = None

# ==============================================================================
# QUERY ANALYZER SETTINGS
# ==============================================================================

MAX_COMPANIES = 10

ENABLE_MULTI_COMPANY = True

CASE_INSENSITIVE = True

# ==============================================================================
# LOGGING
# ==============================================================================

LOGGER_NAME = "QueryAnalyzer"

LOG_LEVEL = "INFO"