"""
==============================================================================
Professional Research Report Parser

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Parses the raw Gemini markdown response into a structured
ResearchReport object.

Responsibilities
----------------
1. Extract report sections
2. Parse recommendation
3. Parse evidence
4. Parse data sources
5. Populate ResearchReport
==============================================================================
"""

import re

from ai.common.logger import get_logger

from ui.report.report_models import (
    ResearchReport,
    Recommendation,
)

logger = get_logger(__name__)


class ReportParser:
    """
    Converts Gemini markdown into a ResearchReport object.
    """

    ####################################################################

    def parse(
        self,
        report: ResearchReport,
        ai_response: str,
    ) -> ResearchReport:

        logger.info("Parsing AI report...")

        report.executive_summary = self._extract_section(
            ai_response,
            "Executive Summary",
        )

        report.market_snapshot = self._extract_section(
            ai_response,
            "Market Snapshot",
        )

        report.technical_analysis = self._extract_section(
            ai_response,
            "Technical Analysis",
        )

        report.fundamental_analysis = self._extract_section(
            ai_response,
            "Fundamental Analysis",
        )

        report.news_intelligence = self._extract_section(
            ai_response,
            "News Intelligence",
        )

        report.sentiment_analysis = self._extract_section(
            ai_response,
            "Sentiment Analysis",
        )

        report.risk_assessment = self._extract_section(
            ai_response,
            "Risk Assessment",
        )

        report.scenario_analysis = self._extract_section(
            ai_response,
            "Scenario Analysis",
        )

        report.investment_thesis = self._extract_section(
            ai_response,
            "Investment Thesis",
        )

        report.recommendation = self._parse_recommendation(
            ai_response
        )

        report.raw_response = ai_response

        logger.info("Report parsed successfully.")

        return report

    ####################################################################

    def _extract_section(
        self,
        text: str,
        heading: str,
    ) -> str:

        pattern = (
            rf"#\s*{re.escape(heading)}"
            rf"(.*?)(?=\n# |\Z)"
        )

        match = re.search(
            pattern,
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )

        if match:

            return match.group(1).strip()

        return ""

    ####################################################################

    def _parse_recommendation(
        self,
        text: str,
    ) -> Recommendation:

        recommendation = Recommendation()

        upper = text.upper()

        if "STRONG BUY" in upper:

            recommendation.rating = "STRONG BUY"

        elif "BUY" in upper:

            recommendation.rating = "BUY"

        elif "HOLD" in upper:

            recommendation.rating = "HOLD"

        elif "SELL" in upper:

            recommendation.rating = "SELL"

        elif "STRONG SELL" in upper:

            recommendation.rating = "STRONG SELL"

        else:

            recommendation.rating = "NOT AVAILABLE"

        recommendation.confidence = 0

        recommendation.score = 0

        recommendation.summary = (
            "Recommendation extracted from AI report."
        )

        return recommendation