"""
==============================================================================
Research Report Models
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Data models used by the Professional Research Report module.

Responsibilities
----------------
1. Store report metadata
2. Store AI generated report sections
3. Store recommendation information
4. Store supporting evidence
5. Serve as the common model for:
   - Dashboard Preview
   - PDF Export
   - Future API responses
============================================================================== 
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# =============================================================================
# Recommendation
# =============================================================================

@dataclass
class Recommendation:

    rating: str = ""

    confidence: float = 0.0

    score: float = 0.0

    summary: str = ""


# =============================================================================
# Evidence
# =============================================================================

@dataclass
class Evidence:

    title: str

    source: str

    published_at: str

    sentiment: str

    relevance_score: float

    snippet: str


# =============================================================================
# Research Report
# =============================================================================

@dataclass
class ResearchReport:

    # -------------------------------------------------------------------------
    # Metadata
    # -------------------------------------------------------------------------

    company: str = ""

    report_type: str = ""

    investment_horizon: str = ""

    generated_at: datetime = field(default_factory=datetime.now)

    generated_by: str = "AI Stock Market Intelligence Platform"

    # -------------------------------------------------------------------------
    # Report Sections
    # -------------------------------------------------------------------------

    executive_summary: str = ""

    market_snapshot: str = ""

    technical_analysis: str = ""

    fundamental_analysis: str = ""

    news_intelligence: str = ""

    sentiment_analysis: str = ""

    risk_assessment: str = ""

    scenario_analysis: str = ""

    investment_thesis: str = ""

    conclusion: str = ""

    disclaimer: str = ""

    # -------------------------------------------------------------------------
    # Recommendation
    # -------------------------------------------------------------------------

    recommendation: Optional[Recommendation] = None

    # -------------------------------------------------------------------------
    # Supporting Evidence
    # -------------------------------------------------------------------------

    evidence: List[Evidence] = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Sources
    # -------------------------------------------------------------------------

    data_sources: List[str] = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Charts
    # -------------------------------------------------------------------------

    charts: List = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Tables
    # -------------------------------------------------------------------------

    tables: List = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Original AI Response
    # -------------------------------------------------------------------------

    raw_response: str = ""

    # -------------------------------------------------------------------------
    # Status
    # -------------------------------------------------------------------------

    success: bool = False

    error_message: str = ""