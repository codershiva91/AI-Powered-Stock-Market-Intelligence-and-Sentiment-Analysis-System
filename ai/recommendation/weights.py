"""
Default investment profile weights.
All positive weights should sum to 1.0.
"""

TECHNICAL_WEIGHT = 0.30
FUNDAMENTAL_WEIGHT = 0.30
SENTIMENT_WEIGHT = 0.15
NEWS_WEIGHT = 0.25

# Risk is used as a penalty, not a positive weight.
RISK_PENALTY_WEIGHT = 0.20

BUY_THRESHOLD = 7.5
HOLD_THRESHOLD = 5.5