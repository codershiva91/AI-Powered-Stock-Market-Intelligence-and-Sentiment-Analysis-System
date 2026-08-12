"""
==============================================================================
Risk Analyzer
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Evaluates investment risk using technical indicators, company fundamentals,
market sentiment, and news.

Responsibilities
----------------
1. Analyze financial risk
2. Calculate Risk Score
3. Determine Risk Level
4. Generate Explainable Risks

Risk Score
----------
0.0  -> Very Low Risk
10.0 -> Very High Risk

==============================================================================
"""

from ai.common.logger import get_logger
from ai.recommendation.recommendation_models import RiskResult

logger = get_logger(__name__)


class RiskAnalyzer:
    """
    Calculates overall investment risk.
    """

    def analyze(
        self,
        technical_data: dict,
        fundamental_data: dict,
        sentiment_data: dict,
        news_result=None,
    ) -> RiskResult:

        logger.info("=" * 60)
        logger.info("RISK ANALYZER")
        logger.info("=" * 60)

        risk_score = 0.0
        risks = []

        # ==========================================================
        # Technical Risk
        # ==========================================================

        rsi = technical_data.get("rsi")

        if rsi is not None:

            if rsi >= 75:
                risk_score += 2
                risks.append("RSI indicates overbought conditions.")

            elif rsi <= 25:
                risk_score += 1
                risks.append("RSI indicates oversold conditions.")

        # ==========================================================
        # Volatility Risk
        # ==========================================================

        volatility = technical_data.get("volatility")

        if volatility is not None:

            if volatility > 0.05:
                risk_score += 2
                risks.append("High price volatility detected.")

        # ==========================================================
        # Debt-to-Equity Risk
        # ==========================================================

        debt_equity = fundamental_data.get("debt_to_equity")

        if debt_equity is not None:

            if debt_equity > 2:
                risk_score += 2
                risks.append("High Debt-to-Equity ratio.")

        # ==========================================================
        # Return on Equity Risk
        # ==========================================================

        roe = fundamental_data.get("roe")

        if roe is not None:

            if roe < 10:
                risk_score += 1
                risks.append("Low Return on Equity.")

        # ==========================================================
        # Profit Margin Risk
        # ==========================================================

        profit_margin = fundamental_data.get("profit_margin")

        if profit_margin is not None:

            if profit_margin < 5:
                risk_score += 1
                risks.append("Low profit margin.")

        # ==========================================================
        # News Risk
        # ==========================================================

        if (
            news_result is not None
            and news_result.sentiment == "Negative"
        ):

            risk_score += 2
            risks.append("Recent financial news is negative.")

        # ==========================================================
        # Market Sentiment Risk
        # ==========================================================

        overall_sentiment = str(
            sentiment_data.get(
                "overall_sentiment",
                "Neutral"
            )
        ).capitalize()

        if overall_sentiment == "Negative":

            risk_score += 2
            risks.append("Market sentiment is negative.")

        # ==========================================================
        # Normalize Risk Score
        # ==========================================================

        risk_score = min(10.0, round(risk_score, 2))

        # ==========================================================
        # Risk Level
        # ==========================================================

        if risk_score < 3:

            level = "Low"

        elif risk_score < 7:

            level = "Medium"

        else:

            level = "High"

        # ==========================================================
        # Logging
        # ==========================================================

        logger.info(
            "Risk Analysis Complete | Score=%.2f Level=%s",
            risk_score,
            level,
        )

        # ==========================================================
        # Return Result
        # ==========================================================

        return RiskResult(
            score=risk_score,
            level=level,
            risks=risks,
        )