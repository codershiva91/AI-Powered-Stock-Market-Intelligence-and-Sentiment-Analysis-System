"""
==============================================================================
Professional Research Report PDF Exporter
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Exports a ResearchReport object into a professional PDF report.

Responsibilities
----------------
1. Create PDF
2. Render report metadata
3. Render recommendation
4. Render report sections
5. Render evidence
6. Render data sources

Uses ReportLab.

============================================================================== 
"""

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from reportlab.pdfgen import canvas

from ui.report.report_models import ResearchReport


class PDFExporter:
    """
    Professional Research Report PDF Exporter.
    """

    ###########################################################################

    def export(
        self,
        report: ResearchReport
    ) -> BytesIO:

        buffer = BytesIO()

        document = SimpleDocTemplate(
            buffer
        )

        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]

        title_style.alignment = TA_CENTER

        heading = styles["Heading2"]

        body = styles["BodyText"]

        story = []
        
        

        # ==============================================================
        # Cover
        # ==============================================================

        story.append(
            Paragraph(
                "AI Stock Market Intelligence Platform",
                title_style,
            )
        )

        story.append(
            Paragraph(
                "Professional Research Report",
                title_style,
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"<b>{report.company}</b>",
                heading,
            )
        )

        story.append(
            Paragraph(
                f"Report Type : {report.report_type}",
                body,
            )
        )

        story.append(
            Paragraph(
                f"Investment Horizon : {report.investment_horizon}",
                body,
            )
        )

        story.append(
            Paragraph(
                report.generated_at.strftime(
                    "%d %B %Y %I:%M %p"
                ),
                body,
            )
        )

        story.append(Spacer(1, 30))

        # ==============================================================
        # Recommendation
        # ==============================================================

        if report.recommendation:

            story.append(
                Paragraph(
                    "AI Recommendation",
                    heading,
                )
            )

            table = Table(

                [
                    [
                        "Rating",
                        report.recommendation.rating,
                    ],

                    [
                        "Confidence",
                        f"{report.recommendation.confidence:.1f}%",
                    ],

                    [
                        "Score",
                        f"{report.recommendation.score:.1f}",
                    ],
                ]

            )

            table.setStyle(

                TableStyle(

                    [

                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            1,
                            colors.black,
                        ),

                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.lightgrey,
                        ),

                        (
                            "BOTTOMPADDING",
                            (0, 0),
                            (-1, -1),
                            8,
                        ),

                    ]

                )

            )

            story.append(table)

            story.append(Spacer(1, 20))

        # ==============================================================
        # Sections
        # ==============================================================

        self._section(
            story,
            heading,
            body,
            "Executive Summary",
            report.executive_summary,
        )

        self._section(
            story,
            heading,
            body,
            "Market Snapshot",
            report.market_snapshot,
        )

        self._section(
            story,
            heading,
            body,
            "Technical Analysis",
            report.technical_analysis,
        )

        self._section(
            story,
            heading,
            body,
            "Fundamental Analysis",
            report.fundamental_analysis,
        )

        self._section(
            story,
            heading,
            body,
            "News Intelligence",
            report.news_intelligence,
        )

        self._section(
            story,
            heading,
            body,
            "Sentiment Analysis",
            report.sentiment_analysis,
        )

        self._section(
            story,
            heading,
            body,
            "Risk Assessment",
            report.risk_assessment,
        )

        self._section(
            story,
            heading,
            body,
            "Scenario Analysis",
            report.scenario_analysis,
        )

        self._section(
            story,
            heading,
            body,
            "Investment Thesis",
            report.investment_thesis,
        )

        self._section(
            story,
            heading,
            body,
            "Conclusion",
            report.conclusion,
        )

        # ==============================================================
        # Evidence
        # ==============================================================

        if report.evidence:

            story.append(
                Paragraph(
                    "Supporting Evidence",
                    heading,
                )
            )

            for item in report.evidence:

                story.append(
                    Paragraph(
                        f"<b>{item.title}</b>",
                        body,
                    )
                )

                if item.source:
                    story.append(
                        Paragraph(
                            f"Source : {item.source}",
                            body,
                        )
                    )

                if item.published_at:
                    story.append(
                        Paragraph(
                            f"Published : {item.published_at}",
                            body,
                        )
                    )

                if item.sentiment:
                    story.append(
                        Paragraph(
                            f"Sentiment : {item.sentiment}",
                            body,
                        )
                    )

                if item.relevance_score:
                    story.append(
                        Paragraph(
                            f"Relevance Score : {item.relevance_score}",
                            body,
                        )
                    )

                if item.snippet:
                    story.append(
                        Paragraph(
                            item.snippet,
                            body,
                        )
                    )

                story.append(Spacer(1, 10))

        # ==============================================================
        # Data Sources
        # ==============================================================

        if report.data_sources:

            story.append(
                Paragraph(
                    "Data Sources",
                    heading,
                )
            )

            for source in report.data_sources:

                story.append(
                    Paragraph(
                        f"• {source}",
                        body,
                    )
                )

            story.append(Spacer(1, 20))

        # ==============================================================
        # Disclaimer
        # ==============================================================

        story.append(
            Paragraph(
                "Disclaimer",
                heading,
            )
        )

        story.append(
            Paragraph(
                report.disclaimer
                if report.disclaimer
                else (
                    "This report has been generated using the AI Stock Market Intelligence Platform. "
                    "It is intended for research and educational purposes only and should not be "
                    "considered financial or investment advice."
                ),
                body,
            )
        )

        # ==============================================================
        # Build PDF
        # ==============================================================

        document.build(story)

        buffer.seek(0)

        return buffer
    
    ###########################################################################

    def _section(
        self,
        story,
        heading,
        body,
        title,
        content,
    ):

        if not content:
            return

        story.append(
            Paragraph(
                title,
                heading,
            )
        )

        # ----------------------------------------------------------
        # String
        # ----------------------------------------------------------

        if isinstance(content, str):

            story.append(
                Paragraph(
                    content,
                    body,
                )
            )

        # ----------------------------------------------------------
        # Dictionary
        # ----------------------------------------------------------

        elif isinstance(content, dict):

            for key, value in content.items():

                if value in ("", None, [], {}):
                    continue

                story.append(
                    Paragraph(
                        f"<b>{key.replace('_', ' ').title()}</b>: {value}",
                        body,
                    )
                )

        # ----------------------------------------------------------
        # List
        # ----------------------------------------------------------

        elif isinstance(content, list):

            for item in content:

                story.append(
                    Paragraph(
                        str(item),
                        body,
                    )
                )

        # ----------------------------------------------------------
        # Fallback
        # ----------------------------------------------------------

        else:

            story.append(
                Paragraph(
                    str(content),
                    body,
                )
            )

        story.append(
            Spacer(1, 15)
        )    