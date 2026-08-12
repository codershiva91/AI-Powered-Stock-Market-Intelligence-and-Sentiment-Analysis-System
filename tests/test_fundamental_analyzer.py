"""
==============================================================================
Unit Tests - Fundamental Analyzer
==============================================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Run:
    python -m pytest tests/test_fundamental_analyzer.py -v

==============================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from ai.recommendation.fundamental_analyzer import FundamentalAnalyzer
from ai.recommendation.recommendation_models import FundamentalResult


# ==========================================================================
# Fixture
# ==========================================================================

@pytest.fixture
def analyzer():
    return FundamentalAnalyzer()


# ==========================================================================
# Test 1 : Missing Fundamental Data
# ==========================================================================

def test_missing_fundamental_data(analyzer):

    result = analyzer.analyze({})

    assert isinstance(result, FundamentalResult)
    assert result.score == 0
    assert len(result.risks) == 1
    assert "Fundamental data is unavailable." in result.risks


# ==========================================================================
# Test 2 : Strong Fundamentals
# ==========================================================================

def test_strong_fundamentals(analyzer):

    data = {
        "trailing_pe": 18,
        "forward_pe": 15,
        "price_to_book": 2.5,
        "debt_to_equity": 40,
        "current_ratio": 2.0,
        "quick_ratio": 1.8,
        "operating_margin": 0.22,
        "profit_margin": 0.18,
        "return_on_equity": 0.25,
        "dividend_yield": 0.03,
    }

    result = analyzer.analyze(data)

    assert isinstance(result, FundamentalResult)
    assert result.score > 0
    assert len(result.reasons) >= 8


# ==========================================================================
# Test 3 : Weak Fundamentals
# ==========================================================================

def test_weak_fundamentals(analyzer):

    data = {
        "trailing_pe": 60,
        "forward_pe": 70,
        "price_to_book": 8,
        "debt_to_equity": 180,
        "current_ratio": 0.7,
        "quick_ratio": 0.6,
        "operating_margin": 0.05,
        "profit_margin": 0.03,
        "return_on_equity": 0.05,
        "dividend_yield": 0,
    }

    result = analyzer.analyze(data)

    assert result.score < 0
    assert len(result.risks) >= 8


# ==========================================================================
# Test 4 : Low PE Ratio
# ==========================================================================

def test_low_pe(analyzer):

    data = {
        "trailing_pe": 18
    }

    result = analyzer.analyze(data)

    assert any(
        "reasonable valuation" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 5 : High PE Ratio
# ==========================================================================

def test_high_pe(analyzer):

    data = {
        "trailing_pe": 50
    }

    result = analyzer.analyze(data)

    assert any(
        "expensive valuation" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 6 : Healthy Debt
# ==========================================================================

def test_healthy_debt(analyzer):

    data = {
        "debt_to_equity": 45
    }

    result = analyzer.analyze(data)

    assert any(
        "healthy range" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 7 : High Debt
# ==========================================================================

def test_high_debt(analyzer):

    data = {
        "debt_to_equity": 150
    }

    result = analyzer.analyze(data)

    assert any(
        "financial risk" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 8 : Strong Liquidity
# ==========================================================================

def test_good_liquidity(analyzer):

    data = {
        "current_ratio": 2.1,
        "quick_ratio": 1.7,
    }

    result = analyzer.analyze(data)

    assert any(
        "liquidity" in reason.lower()
        for reason in result.reasons
    )

    assert any(
        "quick ratio" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 9 : Strong ROE
# ==========================================================================

def test_strong_roe(analyzer):

    data = {
        "return_on_equity": 0.24
    }

    result = analyzer.analyze(data)

    assert any(
        "return on equity" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 10 : Output Structure
# ==========================================================================

def test_output_structure(analyzer):

    data = {
        "trailing_pe": 22,
        "return_on_equity": 0.18
    }

    result = analyzer.analyze(data)

    assert isinstance(result.score, float)
    assert isinstance(result.reasons, list)
    assert isinstance(result.risks, list)


# ==========================================================================
# Test 11 : Partial Data
# ==========================================================================

def test_partial_data(analyzer):

    data = {
        "trailing_pe": 20,
        "return_on_equity": 0.20
    }

    result = analyzer.analyze(data)

    assert result.score > 0


# ==========================================================================
# Test 12 : Dividend Yield
# ==========================================================================

def test_dividend_yield(analyzer):

    data = {
        "dividend_yield": 0.025
    }

    result = analyzer.analyze(data)

    assert any(
        "shareholder returns" in reason.lower()
        for reason in result.reasons
    )