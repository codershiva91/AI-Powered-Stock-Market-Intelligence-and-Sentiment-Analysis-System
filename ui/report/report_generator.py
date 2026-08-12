"""
==============================================================================
Professional Research Report Generator
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Generates professional research reports using the existing AI pipeline.

Responsibilities
----------------
1. Read report configuration
2. Build AI prompt
3. Call SupervisorAgent
4. Generate ResearchReport object
5. Return report to UI

This module DOES NOT modify the AI pipeline.
It simply reuses it.
==============================================================================
"""

from datetime import datetime

from ai.agents.supervisor.supervisor import SupervisorAgent

from ui.report.prompt_builder import ReportPromptBuilder

from ai.common.logger import get_logger

from ui.report.json_validator import JSONValidator

from ui.report.report_models import (
    ResearchReport,
    Recommendation,
    Evidence,
)

logger = get_logger(__name__)


class ResearchReportGenerator:
    """
    Professional Research Report Generator.
    """

    ###########################################################################

    def __init__(self):

        logger.info("Initializing Research Report Generator...")

        self.supervisor = SupervisorAgent()

        self.prompt_builder = ReportPromptBuilder()

        self.validator = JSONValidator()

        logger.info("Research Report Generator initialized.")

    ###########################################################################

    def generate(
        self,
        config: dict,
    ) -> ResearchReport:
        """
        Generate a professional research report.
        """

        report = ResearchReport()

        try:

            logger.info("=" * 80)
            logger.info("GENERATING PROFESSIONAL REPORT")
            logger.info("=" * 80)

            # ==========================================================
            # Metadata
            # ==========================================================

            report.company = config["company"]
            report.report_type = config["report_type"]
            report.investment_horizon = config["investment_horizon"]
            report.generated_at = datetime.now()

            # ==========================================================
            # Build Prompt
            # ==========================================================

            logger.info("Building report prompt...")

            prompt = self.prompt_builder.build(config)

            # ==========================================================
            # Execute AI Pipeline
            # ==========================================================

            logger.info("Executing AI pipeline...")

            ai_response = self.supervisor.answer(prompt)

            logger.info("AI response received.")

            # ==========================================================
            # Validate JSON
            # ==========================================================

            data = self.validator.validate(ai_response)

            # ==========================================================
            # Metadata
            # ==========================================================

            report.company = data.get(
                "company",
                report.company,
            )

            report.report_type = data.get(
                "report_type",
                report.report_type,
            )

            report.investment_horizon = data.get(
                "investment_horizon",
                report.investment_horizon,
            )

            # ==========================================================
            # Recommendation
            # ==========================================================

            recommendation = data.get(
                "recommendation",
                {}
            )

            report.recommendation = Recommendation(

                rating=recommendation.get(
                    "rating",
                    "",
                ),

                confidence=float(
                    recommendation.get(
                        "confidence",
                        0,
                    )
                ),

                score=float(
                    recommendation.get(
                        "score",
                        0,
                    )
                ),

                summary=recommendation.get(
                    "summary",
                    "",
                ),

            )

            # ==========================================================
            # Sections
            # ==========================================================

            report.executive_summary = data.get(
                "executive_summary",
                "",
            )

            report.market_snapshot = data.get(
                "market_snapshot",
                "",
            )

            report.technical_analysis = data.get(
                "technical_analysis",
                "",
            )

            report.fundamental_analysis = data.get(
                "fundamental_analysis",
                "",
            )

            report.news_intelligence = data.get(
                "news_intelligence",
                "",
            )

            report.sentiment_analysis = data.get(
                "sentiment_analysis",
                "",
            )

            report.risk_assessment = data.get(
                "risk_assessment",
                "",
            )

            report.scenario_analysis = data.get(
                "scenario_analysis",
                "",
            )

            report.investment_thesis = data.get(
                "investment_thesis",
                "",
            )

            report.conclusion = data.get(
                "conclusion",
                "",
            )

            report.disclaimer = data.get(
                "disclaimer",
                "",
            )

            # ==========================================================
            # Evidence
            # ==========================================================

            report.evidence = []

            for item in data.get("evidence", []):

                report.evidence.append(

                    Evidence(

                        title=item.get(
                            "title",
                            "",
                        ),

                        source=item.get(
                            "source",
                            "",
                        ),

                        published_at=item.get(
                            "published_at",
                            "",
                        ),

                        sentiment=item.get(
                            "sentiment",
                            "",
                        ),

                        relevance_score=float(
                            item.get(
                                "relevance_score",
                                0,
                            )
                        ),

                        snippet=item.get(
                            "snippet",
                            "",
                        ),

                    )

                )

            # ==========================================================
            # Data Sources
            # ==========================================================

            report.data_sources = data.get(
                "data_sources",
                [],
            )

            # ==========================================================
            # Raw Response
            # ==========================================================

            report.raw_response = ai_response

            report.success = True

            logger.info(
                "Research report generated successfully."
            )

            return report

        except Exception as e:

            logger.exception(
                "Research Report Generation Failed."
            )

            report.success = False

            report.error_message = str(e)

            return report