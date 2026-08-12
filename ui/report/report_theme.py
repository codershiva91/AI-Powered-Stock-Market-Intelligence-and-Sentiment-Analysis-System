"""
==============================================================================
Professional Research Report Theme
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Centralized styling configuration for the Professional Research Report.

Responsibilities
----------------
1. Report colors
2. Recommendation colors
3. Icons
4. Titles
5. Section formatting
6. Dashboard & PDF consistency
==============================================================================
"""

from dataclasses import dataclass


# =============================================================================
# Recommendation Colors
# =============================================================================

RECOMMENDATION_COLORS = {

    "STRONG BUY": "#008000",
    "BUY": "#28A745",
    "HOLD": "#FFC107",
    "SELL": "#FD7E14",
    "STRONG SELL": "#DC3545"

}


# =============================================================================
# Recommendation Icons
# =============================================================================

RECOMMENDATION_ICONS = {

    "STRONG BUY": "🟢",

    "BUY": "🟢",

    "HOLD": "🟡",

    "SELL": "🟠",

    "STRONG SELL": "🔴"

}


# =============================================================================
# Report Theme
# =============================================================================

@dataclass
class ReportTheme:

    # -------------------------------------------------------------------------
    # Typography
    # -------------------------------------------------------------------------

    title_size = 30

    heading_size = 22

    sub_heading_size = 18

    body_size = 14

    caption_size = 12

    # -------------------------------------------------------------------------
    # Spacing
    # -------------------------------------------------------------------------

    section_spacing = 20

    paragraph_spacing = 10

    divider_spacing = 15

    # -------------------------------------------------------------------------
    # Colors
    # -------------------------------------------------------------------------

    primary_color = "#1F77B4"

    secondary_color = "#4F4F4F"

    success_color = "#28A745"

    warning_color = "#FFC107"

    danger_color = "#DC3545"

    background = "#FFFFFF"

    # -------------------------------------------------------------------------
    # Headers
    # -------------------------------------------------------------------------

    report_title = "Professional Research Report"

    executive_title = "Executive Summary"

    technical_title = "Technical Analysis"

    fundamental_title = "Fundamental Analysis"

    market_title = "Market Snapshot"

    news_title = "News Intelligence"

    sentiment_title = "Sentiment Analysis"

    recommendation_title = "AI Recommendation"

    risk_title = "Risk Assessment"

    thesis_title = "Investment Thesis"

    evidence_title = "Supporting Evidence"

    source_title = "Data Sources"

    disclaimer_title = "Disclaimer"

    # -------------------------------------------------------------------------
    # PDF
    # -------------------------------------------------------------------------

    pdf_margin = 50

    pdf_font = "Helvetica"

    pdf_title_size = 20

    pdf_heading_size = 16

    pdf_body_size = 11