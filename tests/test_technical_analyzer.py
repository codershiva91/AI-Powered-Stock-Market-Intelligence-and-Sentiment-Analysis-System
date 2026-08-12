"""
==============================================================================
Unit Tests - Technical Analyzer
==============================================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Run:
    python -m pytest tests/test_technical_analyzer.py -v

==============================================================================
"""

import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Add Project Root to Python Path
# --------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# --------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------

import pytest

from ai.recommendation.technical_analyzer import TechnicalAnalyzer
from ai.recommendation.recommendation_models import TechnicalResult


# ==========================================================================
# Fixture
# ==========================================================================

@pytest.fixture
def analyzer():
    return TechnicalAnalyzer()


# ==========================================================================
# Test 1 : Missing Technical Data
# ==========================================================================

def test_missing_technical_data(analyzer):

    stock_data = {
        "close_price": 1000
    }

    result = analyzer.analyze({}, stock_data)

    assert isinstance(result, TechnicalResult)
    assert result.score == 0
    assert len(result.risks) == 1
    assert "Technical indicators are unavailable." in result.risks


# ==========================================================================
# Test 2 : Strong Bullish Scenario
# ==========================================================================

def test_bullish_analysis(analyzer):

    technical_data = {
        "rsi_14": 25,
        "macd": 2.5,
        "macd_signal": 1.2,
        "sma_20": 1010,
        "sma_50": 980,
        "ema_20": 990,
        "bb_upper": 1050,
        "bb_lower": 900,
    }

    stock_data = {
        "close_price": 1005
    }

    result = analyzer.analyze(technical_data, stock_data)

    assert isinstance(result, TechnicalResult)
    assert result.score > 0

    assert any(
        "oversold" in reason.lower()
        for reason in result.reasons
    )

    assert any(
        "bullish crossover" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 3 : Strong Bearish Scenario
# ==========================================================================

def test_bearish_analysis(analyzer):

    technical_data = {
        "rsi_14": 80,
        "macd": -1.5,
        "macd_signal": -0.5,
        "sma_20": 900,
        "sma_50": 980,
        "ema_20": 1020,
        "bb_upper": 1100,
        "bb_lower": 950,
    }

    stock_data = {
        "close_price": 930
    }

    result = analyzer.analyze(technical_data, stock_data)

    assert isinstance(result, TechnicalResult)

    assert len(result.risks) >= 3

    assert any(
        "overbought" in risk.lower()
        for risk in result.risks
    )

    assert any(
        "bearish crossover" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 4 : Neutral Scenario
# ==========================================================================

def test_neutral_analysis(analyzer):

    technical_data = {
        "rsi_14": 50,
        "macd": 0.6,
        "macd_signal": 0.5,
        "sma_20": 1001,
        "sma_50": 1000,
        "ema_20": 999,
        "bb_upper": 1050,
        "bb_lower": 950,
    }

    stock_data = {
        "close_price": 1000
    }

    result = analyzer.analyze(
        technical_data,
        stock_data
    )

    assert isinstance(result, TechnicalResult)
    assert result.score >= 0

    assert any(
        "healthy trading range" in reason.lower()
        for reason in result.reasons
    )

# ==========================================================================
# Test 5 : Bollinger Upper Breakout
# ==========================================================================

def test_bollinger_breakout(analyzer):

    technical_data = {
        "rsi_14": 45,
        "macd": 1,
        "macd_signal": 0.5,
        "sma_20": 1000,
        "sma_50": 950,
        "ema_20": 990,
        "bb_upper": 1050,
        "bb_lower": 900,
    }

    stock_data = {
        "close_price": 1100
    }

    result = analyzer.analyze(technical_data, stock_data)

    assert any(
        "upper bollinger" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 6 : Bollinger Breakdown
# ==========================================================================

def test_bollinger_breakdown(analyzer):

    technical_data = {
        "rsi_14": 40,
        "macd": -1,
        "macd_signal": -0.5,
        "sma_20": 900,
        "sma_50": 950,
        "ema_20": 980,
        "bb_upper": 1050,
        "bb_lower": 900,
    }

    stock_data = {
        "close_price": 850
    }

    result = analyzer.analyze(technical_data, stock_data)

    assert any(
        "lower bollinger" in risk.lower()
        for risk in result.risks
    )


# ==========================================================================
# Test 7 : RSI Healthy Range
# ==========================================================================

def test_rsi_healthy(analyzer):

    technical_data = {
        "rsi_14": 55,
        "macd": 1,
        "macd_signal": 0.8,
        "sma_20": 1000,
        "sma_50": 990,
        "ema_20": 980,
        "bb_upper": 1050,
        "bb_lower": 900,
    }

    stock_data = {
        "close_price": 1000
    }

    result = analyzer.analyze(technical_data, stock_data)

    assert any(
        "healthy trading range" in reason.lower()
        for reason in result.reasons
    )


# ==========================================================================
# Test 8 : Output Structure
# ==========================================================================

def test_output_structure(analyzer):

    technical_data = {
        "rsi_14": 45,
        "macd": 0.5,
        "macd_signal": 0.4,
        "sma_20": 1000,
        "sma_50": 980,
        "ema_20": 980,
        "bb_upper": 1050,
        "bb_lower": 900,
    }

    stock_data = {
        "close_price": 1000
    }

    result = analyzer.analyze(technical_data, stock_data)

    assert isinstance(result.score, float)
    assert isinstance(result.reasons, list)
    assert isinstance(result.risks, list)