"""
formatter.py
============

Formats Semantic Search results for display.

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence System
"""

from typing import List, Dict


class SearchResultFormatter:
    """
    Formats semantic search results into a readable console output.
    """

    @staticmethod
    def format_console(results: List[Dict]) -> str:
        """
        Format search results.

        Parameters
        ----------
        results : List[Dict]

        Returns
        -------
        str
        """

        if not results:
            return "\nNo search results found.\n"

        output = []
        separator = "=" * 80

        output.append(separator)
        output.append("SEMANTIC SEARCH RESULTS")
        output.append(separator)

        for index, result in enumerate(results, start=1):

            score = result.get("score", 0.0)
            news_id = result.get("news_id") or "N/A"
            title = result.get("title") or "N/A"
            source = result.get("source") or "N/A"
            topic = result.get("topic") or "N/A"
            sentiment = result.get("sentiment") or "N/A"
            published_at = result.get("published_at") or "N/A"
            document = result.get("document") or "No document available."

            output.append("")
            output.append(f"Result #{index}")
            output.append("-" * 80)

            output.append(f"Similarity Score : {float(score):.4f}")
            output.append(f"News ID          : {news_id}")
            output.append(f"Title            : {title}")
            output.append(f"Source           : {source}")
            output.append(f"Topic            : {topic}")
            output.append(f"Sentiment        : {sentiment}")
            output.append(f"Published Date   : {published_at}")

            output.append("")
            output.append("Document")
            output.append("-" * 80)
            output.append(str(document))

            output.append(separator)

        return "\n".join(output)
    
    