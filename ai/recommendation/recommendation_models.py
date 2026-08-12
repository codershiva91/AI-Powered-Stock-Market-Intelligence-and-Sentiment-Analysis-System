"""
==============================================================================
Recommendation Models
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Shared dataclasses used throughout the Recommendation Engine.

These models standardize the output of:

1. Technical Analyzer
2. Fundamental Analyzer
3. Sentiment Analyzer
4. News Analyzer
5. Risk Analyzer
6. Recommendation Engine

==============================================================================
"""

from dataclasses import dataclass, field


# =============================================================================
# Technical Analysis Result
# =============================================================================

@dataclass(slots=True)
class TechnicalResult:
    """
    Technical analysis output.
    """

    score: float = 0.0

    reasons: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)


# =============================================================================
# Fundamental Analysis Result
# =============================================================================

@dataclass(slots=True)
class FundamentalResult:
    """
    Fundamental analysis output.
    """

    score: float = 0.0

    reasons: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)


# =============================================================================
# Sentiment Analysis Result
# =============================================================================

@dataclass(slots=True)
class SentimentResult:
    """
    FinBERT sentiment analysis output.
    """

    score: float = 0.0

    overall_sentiment: str = "Neutral"

    confidence: float = 0.0

    reasons: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)


# =============================================================================
# News Analysis Result
# =============================================================================

@dataclass(slots=True)
class NewsResult:
    """
    News intelligence output.
    """

    score: float = 5.0

    sentiment: str = "Neutral"

    impact: str = "Moderate"

    confidence: float = 0.0

    positive_news: int = 0

    negative_news: int = 0

    neutral_news: int = 0

    total_articles: int = 0

    reasons: list[str] = field(default_factory=list)


# =============================================================================
# Risk Analysis Result
# =============================================================================

@dataclass(slots=True)
class RiskResult:
    """
    Risk analysis output.
    """

    score: float = 0.0

    level: str = "Low"

    risks: list[str] = field(default_factory=list)


# =============================================================================
# Final Recommendation Result
# =============================================================================

@dataclass(slots=True)
class RecommendationResult:
    """
    Final investment recommendation.
    """

    # Final Action

    recommendation: str = "HOLD"

    confidence: float = 0.0

    confidence_level: str = "Medium"

    # Overall Score

    total_score: float = 0.0

    # Individual Scores

    technical_score: float = 0.0

    fundamental_score: float = 0.0

    sentiment_score: float = 0.0

    news_score: float = 0.0

    risk_score: float = 0.0

    # Investment Profile

    investment_style: str = "General"

    # Explainability

    reasons: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)

    supporting_evidence: list[str] = field(default_factory=list)