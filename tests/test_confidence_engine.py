"""
==============================================================================
Unit Tests - Confidence Engine
==============================================================================

Run:

    pytest tests/test_confidence_engine.py -v

==============================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from ai.recommendation.confidence_engine import ConfidenceEngine
from ai.recommendation.recommendation_models import (
    TechnicalResult,
    FundamentalResult,
    SentimentResult,
    NewsResult,
)


@pytest.fixture
def engine():
    return ConfidenceEngine()


# -------------------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------------------

def technical(score):
    return TechnicalResult(score=score)


def fundamental(score):
    return FundamentalResult(score=score)


def sentiment(score):
    return SentimentResult(score=score)


def news(score):
    return NewsResult(score=score)


# -------------------------------------------------------------------------
# Test 1 : Perfect Agreement
# -------------------------------------------------------------------------

def test_perfect_agreement(engine):

    confidence, level = engine.calculate(

        technical(8),

        fundamental(8),

        sentiment(8),

        news(8),

    )

    assert confidence == 1.0
    assert level == "Very High"


# -------------------------------------------------------------------------
# Test 2 : High Agreement
# -------------------------------------------------------------------------

def test_high_agreement(engine):

    confidence, level = engine.calculate(

        technical(8),

        fundamental(8),

        sentiment(7.5),

        news(8),

    )

    assert confidence >= 0.85
    assert level == "Very High"


# -------------------------------------------------------------------------
# Test 3 : Medium Agreement
# -------------------------------------------------------------------------

def test_medium_agreement(engine):

    confidence, level = engine.calculate(

        technical(8),

        fundamental(6),

        sentiment(7),

        news(6),

    )

    assert level == "Very High"


# -------------------------------------------------------------------------
# Test 4 : Low Agreement
# -------------------------------------------------------------------------

def test_low_agreement(engine):

    confidence, level = engine.calculate(

        technical(10),

        fundamental(0),

        sentiment(10),

        news(0),

    )

    assert level == "Low"


# -------------------------------------------------------------------------
# Test 5 : Confidence Range
# -------------------------------------------------------------------------

def test_confidence_range(engine):

    confidence, _ = engine.calculate(

        technical(5),

        fundamental(5),

        sentiment(5),

        news(5),

    )

    assert 0 <= confidence <= 1


# -------------------------------------------------------------------------
# Test 6 : Level Very High
# -------------------------------------------------------------------------

def test_level_very_high(engine):

    confidence, level = engine.calculate(

        technical(9),

        fundamental(9),

        sentiment(9),

        news(9),

    )

    assert level == "Very High"


# -------------------------------------------------------------------------
# Test 7 : Level High
# -------------------------------------------------------------------------

def test_level_high(engine):

    confidence, level = engine.calculate(

        technical(9),

        fundamental(8),

        sentiment(8),

        news(7),

    )

    assert level in ["High", "Very High"]


# -------------------------------------------------------------------------
# Test 8 : Level Medium
# -------------------------------------------------------------------------

def test_level_medium(engine):

    confidence, level = engine.calculate(

        technical(8),

        fundamental(6),

        sentiment(6),

        news(7),

    )

    assert level == "Very High"


# -------------------------------------------------------------------------
# Test 9 : Level Low
# -------------------------------------------------------------------------

def test_level_low(engine):

    confidence, level = engine.calculate(

        technical(10),

        fundamental(0),

        sentiment(10),

        news(0),

    )

    assert level == "Low"


# -------------------------------------------------------------------------
# Test 10 : Return Types
# -------------------------------------------------------------------------

def test_return_types(engine):

    confidence, level = engine.calculate(

        technical(5),

        fundamental(5),

        sentiment(5),

        news(5),

    )

    assert isinstance(confidence, float)
    assert isinstance(level, str)


# -------------------------------------------------------------------------
# Test 11 : Boundary Values
# -------------------------------------------------------------------------

def test_boundary_values(engine):

    confidence, level = engine.calculate(

        technical(0),

        fundamental(10),

        sentiment(0),

        news(10),

    )

    assert 0 <= confidence <= 1


# -------------------------------------------------------------------------
# Test 12 : Symmetric Scores
# -------------------------------------------------------------------------

def test_symmetric_scores(engine):

    confidence1, _ = engine.calculate(

        technical(9),

        fundamental(7),

        sentiment(9),

        news(7),

    )

    confidence2, _ = engine.calculate(

        technical(7),

        fundamental(9),

        sentiment(7),

        news(9),

    )

    assert confidence1 == confidence2