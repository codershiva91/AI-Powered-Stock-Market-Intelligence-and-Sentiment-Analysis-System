"""
==============================================================================
Unit Tests - Sentiment Analyzer
==============================================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Run:
    pytest tests/test_sentiment_analyzer.py -v

==============================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from ai.recommendation.sentiment_analyzer import SentimentAnalyzer
from ai.recommendation.recommendation_models import SentimentResult


# ==========================================================================
# Fixture
# ==========================================================================

@pytest.fixture
def analyzer():
    return SentimentAnalyzer()


# ==========================================================================
# Test 1 : Missing Sentiment Data
# ==========================================================================

def test_missing_sentiment_data(analyzer):

    result = analyzer.analyze({})

    assert isinstance(result, SentimentResult)
    assert result.score == 0
    assert len(result.risks) == 1
    assert "News sentiment data is unavailable." in result.risks


# ==========================================================================
# Test 2 : Strong Positive Sentiment
# ==========================================================================

def test_positive_sentiment(analyzer):

    data = {
        "overall_sentiment": "Positive",
        "confidence": 0.95,
        "positive_count": 25,
        "neutral_count": 5,
        "negative_count": 2,
    }

    result = analyzer.analyze(data)

    assert result.score > 0
    assert result.overall_sentiment == "Positive"
    assert result.confidence == 0.95

    assert any(
        "overall market sentiment is positive" in reason.lower()
        for reason in result.reasons
    )

    assert any(
        "high sentiment confidence" in reason.lower()
        for reason in result.reasons
    )

    assert any(
        "positive news outweighs" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 3 : Strong Negative Sentiment
# ==========================================================================

def test_negative_sentiment(analyzer):

    data = {
        "overall_sentiment": "Negative",
        "confidence": 0.55,
        "positive_count": 3,
        "neutral_count": 2,
        "negative_count": 18,
    }

    result = analyzer.analyze(data)

    assert result.score < 0
    assert result.overall_sentiment == "Negative"

    assert any(
        "overall market sentiment is negative" in risk.lower()
        for risk in result.risks
    )

    assert any(
        "low sentiment confidence" in risk.lower()
        for risk in result.risks
    )

    assert any(
        "negative news outweighs" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 4 : Neutral Sentiment
# ==========================================================================

def test_neutral_sentiment(analyzer):

    data = {
        "overall_sentiment": "Neutral",
        "confidence": 0.75,
        "positive_count": 10,
        "neutral_count": 15,
        "negative_count": 10,
    }

    result = analyzer.analyze(data)

    assert result.overall_sentiment == "Neutral"

    assert any(
        "neutral" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 5 : High Confidence
# ==========================================================================

def test_high_confidence(analyzer):

    data = {
        "overall_sentiment": "Neutral",
        "confidence": 0.93,
    }

    result = analyzer.analyze(data)

    assert any(
        "high sentiment confidence" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 6 : Low Confidence
# ==========================================================================

def test_low_confidence(analyzer):

    data = {
        "overall_sentiment": "Neutral",
        "confidence": 0.45,
    }

    result = analyzer.analyze(data)

    assert any(
        "low sentiment confidence" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 7 : Positive News Dominates
# ==========================================================================

def test_positive_news_dominates(analyzer):

    data = {
        "overall_sentiment": "Neutral",
        "confidence": 0.80,
        "positive_count": 18,
        "neutral_count": 5,
        "negative_count": 2,
    }

    result = analyzer.analyze(data)

    assert any(
        "positive news outweighs" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 8 : Negative News Dominates
# ==========================================================================

def test_negative_news_dominates(analyzer):

    data = {
        "overall_sentiment": "Neutral",
        "confidence": 0.80,
        "positive_count": 2,
        "neutral_count": 4,
        "negative_count": 12,
    }

    result = analyzer.analyze(data)

    assert any(
        "negative news outweighs" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 9 : Equal Positive and Negative News
# ==========================================================================

def test_equal_news(analyzer):

    data = {
        "overall_sentiment": "Neutral",
        "confidence": 0.80,
        "positive_count": 10,
        "neutral_count": 5,
        "negative_count": 10,
    }

    result = analyzer.analyze(data)

    assert result.score == 0


# ==========================================================================
# Test 10 : Output Structure
# ==========================================================================

def test_output_structure(analyzer):

    data = {
        "overall_sentiment": "Positive",
        "confidence": 0.92,
        "positive_count": 10,
        "neutral_count": 2,
        "negative_count": 1,
    }

    result = analyzer.analyze(data)

    assert isinstance(result, SentimentResult)
    assert isinstance(result.score, float)
    assert isinstance(result.reasons, list)
    assert isinstance(result.risks, list)
    assert isinstance(result.overall_sentiment, str)
    assert isinstance(result.confidence, float)


# ==========================================================================
# Test 11 : Default Values
# ==========================================================================

def test_default_values(analyzer):

    result = analyzer.analyze({
        "overall_sentiment": "Neutral"
    })

    assert result.overall_sentiment == "Neutral"
    assert result.confidence == 0.0


# ==========================================================================
# Test 12 : Partial Data
# ==========================================================================

def test_partial_data(analyzer):

    data = {
        "overall_sentiment": "Positive",
        "confidence": 0.91,
    }

    result = analyzer.analyze(data)

    assert result.score > 0