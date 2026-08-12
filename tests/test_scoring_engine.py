"""
==============================================================================
Unit Tests - Scoring Engine
==============================================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Run:

    pytest tests/test_scoring_engine.py -v

==============================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from ai.recommendation.scoring_engine import ScoringEngine

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

    return ScoringEngine()


# =============================================================================
# Helper Functions
# =============================================================================

def technical(score=5):

    return TechnicalResult(
        score=score,
        reasons=["Technical Reason"],
        risks=["Technical Risk"],
    )


def fundamental(score=5):

    return FundamentalResult(
        score=score,
        reasons=["Fundamental Reason"],
        risks=["Fundamental Risk"],
    )


def sentiment(score=5):

    return SentimentResult(
        score=score,
        reasons=["Sentiment Reason"],
        risks=["Sentiment Risk"],
    )


def news(score=5):

    return NewsResult(
        score=score,
        reasons=["News Reason"],
    )


def risk(score=2):

    return RiskResult(
        score=score,
        risks=["Risk Reason"],
    )


# =============================================================================
# Test 1 : Strong Buy
# =============================================================================

def test_strong_buy(engine):

    result = engine.calculate(

        technical(10),

        fundamental(10),

        sentiment(10),

        news(10),

        risk(0),

    )

    assert result.recommendation == "STRONG BUY"


# =============================================================================
# Test 2 : Buy
# =============================================================================

def test_buy(engine):

    result = engine.calculate(

        technical(8),

        fundamental(8),

        sentiment(8),

        news(8),

        risk(1),

    )

    assert result.recommendation in [

        "BUY",

        "STRONG BUY",

    ]


# =============================================================================
# Test 3 : Hold
# =============================================================================

def test_hold(engine):

    result = engine.calculate(

        technical(6),

        fundamental(6),

        sentiment(6),

        news(6),

        risk(3),

    )

    assert result.recommendation == "HOLD"


# =============================================================================
# Test 4 : Sell
# =============================================================================

def test_sell(engine):

    result = engine.calculate(

        technical(4),

        fundamental(4),

        sentiment(4),

        news(4),

        risk(5),

    )

    assert result.recommendation == "SELL"


# =============================================================================
# Test 5 : Strong Sell
# =============================================================================

def test_strong_sell(engine):

    result = engine.calculate(

        technical(1),

        fundamental(1),

        sentiment(1),

        news(1),

        risk(10),

    )

    assert result.recommendation == "STRONG SELL"


# =============================================================================
# Test 6 : Score Never Above 10
# =============================================================================

def test_score_upper_bound(engine):

    result = engine.calculate(

        technical(20),

        fundamental(20),

        sentiment(20),

        news(20),

        risk(0),

    )

    assert result.total_score <= 10


# =============================================================================
# Test 7 : Score Never Below Zero
# =============================================================================

def test_score_lower_bound(engine):

    result = engine.calculate(

        technical(0),

        fundamental(0),

        sentiment(0),

        news(0),

        risk(20),

    )

    assert result.total_score >= 0


# =============================================================================
# Test 8 : Confidence Exists
# =============================================================================

def test_confidence(engine):

    result = engine.calculate(

        technical(),

        fundamental(),

        sentiment(),

        news(),

        risk(),

    )

    assert result.confidence >= 0
    assert result.confidence <= 1


# =============================================================================
# Test 9 : Reasons Combined
# =============================================================================

def test_reasons(engine):

    result = engine.calculate(

        technical(),

        fundamental(),

        sentiment(),

        news(),

        risk(),

    )

    assert "Technical Reason" in result.reasons
    assert "Fundamental Reason" in result.reasons
    assert "Sentiment Reason" in result.reasons
    assert "News Reason" in result.reasons


# =============================================================================
# Test 10 : Risks Combined
# =============================================================================

def test_risks(engine):

    result = engine.calculate(

        technical(),

        fundamental(),

        sentiment(),

        news(),

        risk(),

    )

    assert "Technical Risk" in result.risks
    assert "Fundamental Risk" in result.risks
    assert "Sentiment Risk" in result.risks
    assert "Risk Reason" in result.risks


# =============================================================================
# Test 11 : Duplicate Removal
# =============================================================================

def test_duplicate_removal(engine):

    t = TechnicalResult(

        score=5,

        reasons=["Same"],

        risks=["Risk"],

    )

    f = FundamentalResult(

        score=5,

        reasons=["Same"],

        risks=["Risk"],

    )

    s = SentimentResult(

        score=5,

        reasons=["Same"],

        risks=["Risk"],

    )

    n = NewsResult(

        score=5,

        reasons=["Same"],

    )

    r = RiskResult(

        score=2,

        risks=["Risk"],

    )

    result = engine.calculate(

        t,

        f,

        s,

        n,

        r,

    )

    assert result.reasons.count("Same") == 1
    assert result.risks.count("Risk") == 1


# =============================================================================
# Test 12 : Output Structure
# =============================================================================

def test_output_structure(engine):

    result = engine.calculate(

        technical(),

        fundamental(),

        sentiment(),

        news(),

        risk(),

    )

    assert isinstance(result, RecommendationResult)

    assert isinstance(result.total_score, float)

    assert isinstance(result.recommendation, str)

    assert isinstance(result.confidence, float)

    assert isinstance(result.reasons, list)

    assert isinstance(result.risks, list)