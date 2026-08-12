"""
==============================================================================
Unit Tests - News Analyzer
==============================================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Run:
    pytest tests/test_news_analyzer.py -v

==============================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from ai.recommendation.news_analyzer import NewsAnalyzer
from ai.recommendation.recommendation_models import NewsResult


# ==========================================================================
# Fixture
# ==========================================================================

@pytest.fixture
def analyzer():
    return NewsAnalyzer()


# ==========================================================================
# Test 1 : No News
# ==========================================================================

def test_no_news(analyzer):

    result = analyzer.analyze([])

    assert isinstance(result, NewsResult)
    assert result.score == 5.0
    assert result.sentiment == "Neutral"
    assert result.impact == "Low"
    assert result.total_articles == 0

    assert any(
        "no recent financial news" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 2 : All Positive News
# ==========================================================================

def test_all_positive_news(analyzer):

    documents = [

        {
            "title": "Strong Earnings",
            "sentiment": "Positive",
            "confidence": 0.95,
            "relevance_score": 1.0,
        },

        {
            "title": "Expansion",
            "sentiment": "Positive",
            "confidence": 0.90,
            "relevance_score": 0.90,
        },
    ]

    result = analyzer.analyze(documents)

    assert result.sentiment == "Positive"
    assert result.impact in ["High", "Moderate"]
    assert result.positive_news == 2
    assert result.negative_news == 0
    assert result.total_articles == 2
    assert result.score > 5


# ==========================================================================
# Test 3 : All Negative News
# ==========================================================================

def test_all_negative_news(analyzer):

    documents = [

        {
            "title": "Fraud Investigation",
            "sentiment": "Negative",
            "confidence": 1.0,
            "relevance_score": 1.0,
        },

        {
            "title": "Profit Warning",
            "sentiment": "Negative",
            "confidence": 0.95,
            "relevance_score": 0.90,
        },
    ]

    result = analyzer.analyze(documents)

    assert result.sentiment == "Negative"
    assert result.negative_news == 2
    assert result.score < 4


# ==========================================================================
# Test 4 : Neutral News
# ==========================================================================

def test_neutral_news(analyzer):

    documents = [

        {
            "title": "Quarterly Meeting",
            "sentiment": "Neutral",
            "confidence": 1.0,
            "relevance_score": 1.0,
        }

    ]

    result = analyzer.analyze(documents)

    assert result.sentiment == "Neutral"
    assert result.score == 5.0
    assert result.neutral_news == 1


# ==========================================================================
# Test 5 : Mixed News
# ==========================================================================

def test_mixed_news(analyzer):

    documents = [

        {
            "title": "Good Results",
            "sentiment": "Positive",
            "confidence": 0.95,
            "relevance_score": 1.0,
        },

        {
            "title": "CEO Resigns",
            "sentiment": "Negative",
            "confidence": 0.90,
            "relevance_score": 1.0,
        },

        {
            "title": "Product Launch",
            "sentiment": "Neutral",
            "confidence": 0.90,
            "relevance_score": 1.0,
        }

    ]

    result = analyzer.analyze(documents)

    assert result.total_articles == 3
    assert result.positive_news == 1
    assert result.negative_news == 1
    assert result.neutral_news == 1


# ==========================================================================
# Test 6 : Confidence Calculation
# ==========================================================================

def test_confidence(analyzer):

    documents = []

    for i in range(5):

        documents.append({

            "title": f"News {i}",

            "sentiment": "Positive",

            "confidence": 1.0,

            "relevance_score": 1.0

        })

    result = analyzer.analyze(documents)

    assert result.confidence == 0.5


# ==========================================================================
# Test 7 : Confidence Cap
# ==========================================================================

def test_confidence_cap(analyzer):

    documents = []

    for i in range(20):

        documents.append({

            "title": f"News {i}",

            "sentiment": "Positive",

            "confidence": 1.0,

            "relevance_score": 1.0

        })

    result = analyzer.analyze(documents)

    assert result.confidence == 1.0


# ==========================================================================
# Test 8 : Reasons Limit
# ==========================================================================

def test_reason_limit(analyzer):

    documents = []

    for i in range(10):

        documents.append({

            "title": f"Positive News {i}",

            "sentiment": "Positive",

            "confidence": 1.0,

            "relevance_score": 1.0

        })

    result = analyzer.analyze(documents)

    assert len(result.reasons) == 5


# ==========================================================================
# Test 9 : Default Values
# ==========================================================================

def test_default_values(analyzer):

    documents = [

        {}

    ]

    result = analyzer.analyze(documents)

    assert result.total_articles == 1
    assert result.sentiment == "Neutral"


# ==========================================================================
# Test 10 : Weighted Positive Score
# ==========================================================================

def test_weighted_score(analyzer):

    documents = [

        {
            "title": "High Confidence",

            "sentiment": "Positive",

            "confidence": 1.0,

            "relevance_score": 1.0

        },

        {
            "title": "Low Confidence",

            "sentiment": "Positive",

            "confidence": 0.20,

            "relevance_score": 0.20

        }

    ]

    result = analyzer.analyze(documents)

    assert result.score > 5


# ==========================================================================
# Test 11 : Output Structure
# ==========================================================================

def test_output_structure(analyzer):

    result = analyzer.analyze([])

    assert isinstance(result, NewsResult)

    assert isinstance(result.score, float)

    assert isinstance(result.sentiment, str)

    assert isinstance(result.impact, str)

    assert isinstance(result.confidence, float)

    assert isinstance(result.total_articles, int)

    assert isinstance(result.reasons, list)


# ==========================================================================
# Test 12 : Case Insensitive Sentiment
# ==========================================================================

def test_case_insensitive_sentiment(analyzer):

    documents = [

        {
            "title": "Excellent Results",

            "sentiment": "POSITIVE",

            "confidence": 1.0,

            "relevance_score": 1.0

        }

    ]

    result = analyzer.analyze(documents)

    assert result.positive_news == 1
    assert result.sentiment == "Positive"