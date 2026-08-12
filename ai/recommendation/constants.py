"""
==============================================================================
Recommendation Engine Constants
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Shared constants used across the recommendation engine.

==============================================================================
"""

# =============================================================================
# Recommendation Weights
# =============================================================================

# Total Positive Weight = 1.00

TECHNICAL_WEIGHT = 0.30
FUNDAMENTAL_WEIGHT = 0.30
SENTIMENT_WEIGHT = 0.20
NEWS_WEIGHT = 0.20

# Risk Penalty Weight
RISK_PENALTY_WEIGHT = 0.10

# =============================================================================
# Recommendation Thresholds
# =============================================================================

BUY_THRESHOLD = 7.5
HOLD_THRESHOLD = 5.0

# =============================================================================
# Technical Analysis
# =============================================================================

RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70

# =============================================================================
# Technical Indicator Scores
# =============================================================================

TECHNICAL_SCORE = {

    # RSI
    "RSI_BULLISH": 2,
    "RSI_BEARISH": -2,

    # MACD
    "MACD_BULLISH": 2,
    "MACD_BEARISH": -2,

    # SMA
    "SMA_GOLDEN_CROSS": 2,
    "SMA_DEATH_CROSS": -2,

    # EMA
    "PRICE_ABOVE_EMA": 1,
    "PRICE_BELOW_EMA": -1,

    # Bollinger Bands
    "BOLLINGER_BREAKOUT": 1,
    "BOLLINGER_BREAKDOWN": -1,
}