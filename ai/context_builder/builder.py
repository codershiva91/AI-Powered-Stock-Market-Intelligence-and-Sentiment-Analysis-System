"""
==============================================================================
Context Builder
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Builds the final context passed to the LLM.

Responsibilities
----------------
1. Read reranked documents
2. Remove empty articles
3. Format documents
4. Limit context size
5. Return final context

==============================================================================
"""

from typing import List, Dict

from .logger import get_logger
from .exceptions import ContextBuilderError

logger = get_logger(__name__)


class ContextBuilder:

    def __init__(self):

        logger.info("Context Builder initialized.")

    ##################################################################

    def build(
        self,
        documents: List[Dict],
        max_documents: int = 5,
        max_article_chars: int = 1500,
    ) -> str:

        try:

            if not documents:
                return "No relevant documents found."

            context_parts = []

            for index, doc in enumerate(documents[:max_documents], start=1):

                title = doc.get("title", "Untitled")

                source = doc.get("source", "Unknown Source")

                published_at = doc.get("published_at", "Unknown Date")

                article = doc.get("article_text", "")

                article = article.strip()

                if not article:
                    article = "No article text available."

                article = article[:max_article_chars]

                context_parts.append(
                    f"""
Article {index}

Title:
{title}

Source:
{source}

Published:
{published_at}

Content:
{article}
""".strip()
                )

            context = "\n\n" + ("=" * 80) + "\n\n"

            context = context.join(context_parts)

            logger.info(
                "Context built successfully with %d documents.",
                len(context_parts),
            )

            return context

        except Exception as e:

            logger.exception("Context Builder failed.")

            raise ContextBuilderError(str(e))