"""
==============================================================================
Unit Tests - Recommendation Engine
==============================================================================

Run:

    pytest test_recommendation_engine.py -v

==============================================================================
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from ai.recommendation.recommendation_engine import RecommendationEngine
from ai.recommendation.recommendation_models import (
    TechnicalResult,
    FundamentalResult,
    SentimentResult,
    NewsResult,
    RiskResult,
    RecommendationResult,
)


# =============================================================================
# Fixture
# =============================================================================

@pytest.fixture
def engine():

    engine = RecommendationEngine()

    engine.technical_analyzer = MagicMock()
    engine.fundamental_analyzer = MagicMock()
    engine.sentiment_analyzer = MagicMock()
    engine.news_analyzer = MagicMock()
    engine.risk_analyzer = MagicMock()
    engine.scoring_engine = MagicMock()

    return engine


# =============================================================================
# Dummy Objects
# =============================================================================

technical_result = TechnicalResult(
    score=8.0,
    reasons=["RSI Bullish"],
    risks=[]
)

fundamental_result = FundamentalResult(
    score=7.5,
    reasons=["Good PE"],
    risks=[]
)

sentiment_result = SentimentResult(
    score=7.0,
    overall_sentiment="Positive",
    confidence=0.86,
    reasons=["Positive News"],
    risks=[]
)

news_result = NewsResult(
    score=8.0,
    sentiment="Positive",
    impact="High",
    confidence=0.87,
    positive_news=8,
    negative_news=1,
    neutral_news=1,
    total_articles=10,
    reasons=["Strong Headlines"],
)

risk_result = RiskResult(
    score=2.0,
    level="Low",
    risks=[]
)

recommendation_result = RecommendationResult(
    recommendation="BUY",
    confidence=0.91,
    confidence_level="Very High",

    total_score=8.2,

    technical_score=8.0,
    fundamental_score=7.5,
    sentiment_score=7.0,
    news_score=8.0,
    risk_score=2.0,

    investment_style="Growth",

    reasons=["Good Technical"],
    risks=[],
    supporting_evidence=[]
)


# =============================================================================
# Helper
# =============================================================================

def setup_engine(engine):

    engine.technical_analyzer.analyze.return_value = technical_result

    engine.fundamental_analyzer.analyze.return_value = fundamental_result

    engine.sentiment_analyzer.analyze.return_value = sentiment_result

    engine.news_analyzer.analyze.return_value = news_result

    engine.risk_analyzer.analyze.return_value = risk_result

    engine.scoring_engine.calculate.return_value = recommendation_result


# =============================================================================
# Test 1
# =============================================================================

def test_generate_success(engine):

    setup_engine(engine)

    result = engine.generate({}, {}, {}, {}, [])

    assert result == recommendation_result


# =============================================================================
# Test 2
# =============================================================================

def test_technical_called(engine):

    setup_engine(engine)

    engine.generate({}, {}, {}, {}, [])

    engine.technical_analyzer.analyze.assert_called_once()


# =============================================================================
# Test 3
# =============================================================================

def test_fundamental_called(engine):

    setup_engine(engine)

    engine.generate({}, {}, {}, {}, [])

    engine.fundamental_analyzer.analyze.assert_called_once()


# =============================================================================
# Test 4
# =============================================================================

def test_sentiment_called(engine):

    setup_engine(engine)

    engine.generate({}, {}, {}, {}, [])

    engine.sentiment_analyzer.analyze.assert_called_once()


# =============================================================================
# Test 5
# =============================================================================

def test_news_called(engine):

    setup_engine(engine)

    engine.generate({}, {}, {}, {}, [])

    engine.news_analyzer.analyze.assert_called_once()


# =============================================================================
# Test 6
# =============================================================================

def test_risk_called(engine):

    setup_engine(engine)

    engine.generate({}, {}, {}, {}, [])

    engine.risk_analyzer.analyze.assert_called_once()


# =============================================================================
# Test 7
# =============================================================================

def test_scoring_called(engine):

    setup_engine(engine)

    engine.generate({}, {}, {}, {}, [])

    engine.scoring_engine.calculate.assert_called_once()


# =============================================================================
# Test 8
# =============================================================================

def test_output_type(engine):

    setup_engine(engine)

    result = engine.generate({}, {}, {}, {}, [])

    assert isinstance(result, RecommendationResult)


# =============================================================================
# Test 9
# =============================================================================

def test_empty_inputs(engine):

    setup_engine(engine)

    result = engine.generate(None, None, None, None, None)

    assert result.recommendation == "BUY"


# =============================================================================
# Test 10
# =============================================================================

def test_technical_exception(engine):

    engine.technical_analyzer.analyze.side_effect = Exception(
        "Technical Error"
    )

    with pytest.raises(Exception):

        engine.generate({}, {}, {}, {}, [])


# =============================================================================
# Test 11
# =============================================================================

def test_scoring_exception(engine):

    setup_engine(engine)

    engine.scoring_engine.calculate.side_effect = Exception(
        "Scoring Error"
    )

    with pytest.raises(Exception):

        engine.generate({}, {}, {}, {}, [])


# =============================================================================
# Test 12
# =============================================================================

def test_recommendation_fields(engine):

    setup_engine(engine)

    result = engine.generate({}, {}, {}, {}, [])

    assert result.recommendation == "BUY"

    assert result.total_score == 8.2

    assert result.confidence == 0.91

    assert result.confidence_level == "Very High"

    assert result.investment_style == "Growth"

    assert result.technical_score == 8.0

    assert result.fundamental_score == 7.5

    assert result.sentiment_score == 7.0

    assert result.news_score == 8.0

    assert result.risk_score == 2.0