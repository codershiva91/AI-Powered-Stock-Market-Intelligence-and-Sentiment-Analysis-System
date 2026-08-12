"""
==============================================================================
News Models
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Models used by the News Analyzer.

==============================================================================
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class NewsResult:
    """
    Output of News Analyzer.
    """

    score: float

    sentiment: str

    impact: str

    confidence: float

    reasons: list[str] = field(default_factory=list)

    positive_news: int = 0

    negative_news: int = 0

    neutral_news: int = 0

    total_articles: int = 0