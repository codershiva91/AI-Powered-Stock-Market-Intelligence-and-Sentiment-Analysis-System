"""
==============================================================================
LangGraph Reranker Node
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
==============================================================================
"""

from ai.langgraph.state import GraphState
from ai.cross_encoder.reranker import CrossEncoderReranker
from ai.llm.logger import get_logger

logger = get_logger(__name__)


class RerankerNode:
    """
    LangGraph node for Cross Encoder reranking.
    """

    def __init__(self):
        self.reranker = CrossEncoderReranker()

    def __call__(self, state: GraphState) -> GraphState:

        try:

            logger.info("=" * 60)
            logger.info("RERANKER NODE")
            logger.info("=" * 60)

            question = state.get("question", "")

            documents = state.get("retrieved_documents", [])

            logger.info("Retrieved documents in state : %d", len(documents))

            if not documents:

                logger.warning("No retrieved documents found.")

                state["reranked_documents"] = []
                state["error"] = None

                return state

            ranked_documents = self.reranker.rerank(
                query=question,
                documents=documents
            )

            state["reranked_documents"] = ranked_documents
            state["error"] = None

            logger.info(
                "Successfully reranked %d documents.",
                len(ranked_documents)
            )

            return state

        except Exception as e:

            logger.exception("Reranker Node failed.")

            state["reranked_documents"] = []
            state["error"] = str(e)

            return state