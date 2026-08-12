"""
==============================================================================
Unit Tests - Risk Analyzer
==============================================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Run:
    pytest tests/test_risk_analyzer.py -v

==============================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from ai.recommendation.risk_analyzer import RiskAnalyzer
from ai.recommendation.recommendation_models import RiskResult, NewsResult


# ==========================================================================
# Fixture
# ==========================================================================

@pytest.fixture
def analyzer():
    return RiskAnalyzer()


# ==========================================================================
# Test 1 : No Risk
# ==========================================================================

def test_no_risk(analyzer):

    result = analyzer.analyze(
        technical_data={},
        fundamental_data={},
        sentiment_data={},
        news_result=None,
    )

    assert isinstance(result, RiskResult)
    assert result.score == 0
    assert result.level == "Low"
    assert len(result.risks) == 0


# ==========================================================================
# Test 2 : High RSI Risk
# ==========================================================================

def test_high_rsi(analyzer):

    technical = {
        "rsi": 80
    }

    result = analyzer.analyze(
        technical,
        {},
        {},
        None,
    )

    assert result.score >= 2

    assert any(
        "overbought" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 3 : Oversold RSI
# ==========================================================================

def test_low_rsi(analyzer):

    technical = {
        "rsi": 20
    }

    result = analyzer.analyze(
        technical,
        {},
        {},
        None,
    )

    assert result.score >= 1

    assert any(
        "oversold" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 4 : High Volatility
# ==========================================================================

def test_high_volatility(analyzer):

    technical = {
        "volatility": 0.08
    }

    result = analyzer.analyze(
        technical,
        {},
        {},
        None,
    )

    assert any(
        "volatility" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 5 : High Debt
# ==========================================================================

def test_high_debt(analyzer):

    fundamentals = {
        "debt_to_equity": 3
    }

    result = analyzer.analyze(
        {},
        fundamentals,
        {},
        None,
    )

    assert any(
        "debt-to-equity" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 6 : Low ROE
# ==========================================================================

def test_low_roe(analyzer):

    fundamentals = {
        "roe": 8
    }

    result = analyzer.analyze(
        {},
        fundamentals,
        {},
        None,
    )

    assert any(
        "return on equity" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 7 : Low Profit Margin
# ==========================================================================

def test_low_profit_margin(analyzer):

    fundamentals = {
        "profit_margin": 3
    }

    result = analyzer.analyze(
        {},
        fundamentals,
        {},
        None,
    )

    assert any(
        "profit margin" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 8 : Negative News
# ==========================================================================

def test_negative_news(analyzer):

    news = NewsResult(
        sentiment="Negative"
    )

    result = analyzer.analyze(
        {},
        {},
        {},
        news,
    )

    assert any(
        "financial news" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 9 : Negative Market Sentiment
# ==========================================================================

def test_negative_market_sentiment(analyzer):

    sentiment = {
        "overall_sentiment": "Negative"
    }

    result = analyzer.analyze(
        {},
        {},
        sentiment,
        None,
    )

    assert any(
        "market sentiment" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 10 : High Combined Risk
# ==========================================================================

def test_high_combined_risk(analyzer):

    technical = {
        "rsi": 80,
        "volatility": 0.08,
    }

    fundamentals = {
        "debt_to_equity": 3,
        "roe": 5,
        "profit_margin": 2,
    }

    sentiment = {
        "overall_sentiment": "Negative"
    }

    news = NewsResult(
        sentiment="Negative"
    )

    result = analyzer.analyze(
        technical,
        fundamentals,
        sentiment,
        news,
    )

    assert result.score >= 9
    assert result.level == "High"


# ==========================================================================
# Test 11 : Medium Risk
# ==========================================================================

def test_medium_risk(analyzer):

    technical = {
        "rsi": 80
    }

    fundamentals = {
        "roe": 8
    }

    result = analyzer.analyze(
        technical,
        fundamentals,
        {},
        None,
    )

    assert result.level == "Medium"


# ==========================================================================
# Test 12 : Output Structure
# ==========================================================================

def test_output_structure(analyzer):

    result = analyzer.analyze(
        {},
        {},
        {},
        None,
    )

    assert isinstance(result, RiskResult)
    assert isinstance(result.score, float)
    assert isinstance(result.level, str)
    assert isinstance(result.risks, list)