"""
==============================================================================
News Analyzer
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Analyzes reranked financial news and converts it into a structured
investment signal.

Responsibilities
----------------
1. Analyze financial news sentiment
2. Calculate News Score
3. Determine Market Impact
4. Generate Explainable Reasons
5. Return NewsResult

Score Range
-----------
0.0  -> Extremely Negative
5.0  -> Neutral
10.0 -> Extremely Positive

==============================================================================
"""

from ai.common.logger import get_logger
from ai.recommendation.recommendation_models import NewsResult

logger = get_logger(__name__)


class NewsAnalyzer:
    """
    Analyze financial news retrieved from Qdrant
    after CrossEncoder reranking.
    """

    def analyze(self, documents: list[dict]) -> NewsResult:

        logger.info("=" * 60)
        logger.info("NEWS ANALYZER")
        logger.info("=" * 60)

        # ------------------------------------------------------------------
        # No News Available
        # ------------------------------------------------------------------

        if not documents:

            logger.warning("No news available.")

            return NewsResult(
                score=5.0,
                sentiment="Neutral",
                impact="Low",
                confidence=0.0,
                total_articles=0,
                reasons=[
                    "No recent financial news found."
                ]
            )

        # ------------------------------------------------------------------
        # Counters
        # ------------------------------------------------------------------

        positive = 0
        negative = 0
        neutral = 0

        reasons = []

        weighted_score = 0.0
        total_weight = 0.0

        # ------------------------------------------------------------------
        # Analyze Documents
        # ------------------------------------------------------------------

        for doc in documents:

            sentiment = str(
                doc.get("sentiment", "Neutral")
            ).lower()

            confidence = float(
                doc.get("confidence", 0.5)
            )

            relevance = float(
                doc.get("relevance_score", 1.0)
            )

            title = doc.get(
                "title",
                "Financial News"
            )

            # Weight = Confidence × Relevance
            weight = confidence * relevance

            total_weight += weight

            # --------------------------------------------------------------

            if sentiment == "positive":

                positive += 1

                weighted_score += 10 * weight

                reasons.append(
                    f"Positive: {title}"
                )

            elif sentiment == "negative":

                negative += 1

                weighted_score += 0 * weight

                reasons.append(
                    f"Negative: {title}"
                )

            else:

                neutral += 1

                weighted_score += 5 * weight

        # ------------------------------------------------------------------
        # Final Score
        # ------------------------------------------------------------------

        total_articles = positive + negative + neutral

        if total_articles == 0:

            return NewsResult()

        # ------------------------------------------------------------------
        # Weighted Average
        # ------------------------------------------------------------------

        if total_weight > 0:

            average_score = weighted_score / total_weight

        else:

            average_score = 5.0

        # ------------------------------------------------------------------
        # Sentiment Classification
        # ------------------------------------------------------------------

        if average_score >= 8:

            final_sentiment = "Positive"
            impact = "High"

        elif average_score >= 6:

            final_sentiment = "Positive"
            impact = "Moderate"

        elif average_score >= 4:

            final_sentiment = "Neutral"
            impact = "Moderate"

        else:

            final_sentiment = "Negative"
            impact = "High"

        # ------------------------------------------------------------------
        # Overall Confidence
        # ------------------------------------------------------------------

        overall_confidence = min(
            1.0,
            total_articles / 10
        )

        # ------------------------------------------------------------------
        # Logging
        # ------------------------------------------------------------------

        logger.info(
            "News Analysis Complete | "
            "Positive=%d Negative=%d Neutral=%d Score=%.2f",
            positive,
            negative,
            neutral,
            average_score,
        )

        # ------------------------------------------------------------------
        # Return Result
        # ------------------------------------------------------------------

        return NewsResult(

            score=round(average_score, 2),

            sentiment=final_sentiment,

            impact=impact,

            confidence=round(overall_confidence, 2),

            positive_news=positive,

            negative_news=negative,

            neutral_news=neutral,

            total_articles=total_articles,

            reasons=reasons[:5]

        )