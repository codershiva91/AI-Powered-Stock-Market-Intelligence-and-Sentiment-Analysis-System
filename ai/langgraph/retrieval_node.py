# """
# =========================================================
# LangGraph Retrieval Node
# =========================================================

# Author      : Shivam Sahu
# Project     : AI-Driven Stock Market Intelligence System

# Description
# -----------
# LangGraph node responsible for semantic retrieval
# from the Qdrant Vector Database.

# Responsibilities
# ----------------
# 1. Read GraphState
# 2. Validate user query
# 3. Read metadata filters from Query Analyzer
# 4. Perform semantic retrieval
# 5. Store retrieved documents
# 6. Handle retrieval errors
# 7. Log execution details

# =========================================================
# """

# from ai.langgraph.state import GraphState

# from ai.retriever.retriever import Retriever
# from ai.retriever.config import TOP_K
# from ai.retriever.logger import get_logger

# logger = get_logger(__name__)


# class RetrievalNode:
#     """
#     LangGraph node responsible for semantic retrieval.
#     """

#     ##################################################################

#     def __init__(self):

#         self.retriever = Retriever()

#     ##################################################################

#     def __call__(self, state: GraphState) -> GraphState:

#         try:

#             logger.info("=" * 60)
#             logger.info("RETRIEVAL NODE")
#             logger.info("=" * 60)

#             question = state.get("question", "").strip()

#             if not question:

#                 logger.error("User question is empty.")

#                 state["retrieved_documents"] = []
#                 state["success"] = False
#                 state["error"] = "Question cannot be empty."

#                 return state

#             analysis = state.get("query_analysis", {})

#             filters = analysis.get("filters", {})

#             logger.info("Question : %s", question)
#             logger.info("Filters  : %s", filters)

#             results = self.retriever.search(

#                 query=question,

#                 top_k=TOP_K,

#                 topic=filters.get("topic"),

#                 sentiment=filters.get("sentiment"),

#                 news_type=filters.get("news_type"),

#                 source=filters.get("source"),

#                 published_after=filters.get("published_after"),

#                 published_before=filters.get("published_before"),

#             )

#             state["retrieved_documents"] = results
#             state["success"] = True
#             state["error"] = None

#             logger.info(
#                 "Retrieved %d documents successfully.",
#                 len(results),
#             )

#             return state

#         except Exception as e:

#             logger.exception("Retrieval Node failed.")

#             state["retrieved_documents"] = []
#             state["success"] = False
#             state["error"] = str(e)

#             return state


"""
=========================================================
LangGraph Retrieval Node
=========================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
LangGraph node responsible for semantic retrieval
from the Qdrant Vector Database.

Responsibilities
----------------
1. Read GraphState
2. Validate user query
3. Read metadata filters from Query Analyzer
4. Perform semantic retrieval
5. Store retrieved documents
6. Handle retrieval errors
7. Log execution details

=========================================================
"""

from ai.langgraph.state import GraphState

from ai.retriever.retriever import Retriever
from ai.retriever.config import TOP_K
from ai.retriever.logger import get_logger

logger = get_logger(__name__)


class RetrievalNode:
    """
    LangGraph node responsible for semantic retrieval.
    """

    def __init__(self):
        self.retriever = Retriever()

    def __call__(self, state: GraphState) -> GraphState:

        try:

            logger.info("=" * 60)
            logger.info("RETRIEVAL NODE")
            logger.info("=" * 60)

            # ----------------------------------------------------------
            # Read Question Safely
            # ----------------------------------------------------------

            question = state.get("question", "")

            logger.info("Question Type : %s", type(question).__name__)

            if isinstance(question, dict):

                logger.warning(
                    "Question received as dictionary. Extracting text..."
                )

                question = (
                    question.get("question")
                    or question.get("query")
                    or question.get("text")
                    or ""
                )

            question = str(question).strip()

            if not question:

                logger.error("User question is empty.")

                state["retrieved_documents"] = []
                state["success"] = False
                state["error"] = "Question cannot be empty."

                return state

            # ----------------------------------------------------------
            # Query Analysis
            # ----------------------------------------------------------

            analysis = state.get("query_analysis", {})

            if not isinstance(analysis, dict):
                analysis = {}

            filters = analysis.get("filters", {})

            if not isinstance(filters, dict):
                filters = {}

            logger.info("Question : %s", question)
            logger.info("Filters  : %s", filters)

            # ----------------------------------------------------------
            # Retrieval
            # ----------------------------------------------------------

            results = self.retriever.search(
                query=question,
                top_k=TOP_K,
                topic=filters.get("topic"),
                sentiment=filters.get("sentiment"),
                news_type=filters.get("news_type"),
                source=filters.get("source"),
                published_after=filters.get("published_after"),
                published_before=filters.get("published_before"),
            )

            # ----------------------------------------------------------
            # Save Results
            # ----------------------------------------------------------

            state["retrieved_documents"] = results
            state["success"] = True
            state["error"] = None

            logger.info(
                "Retrieved %d documents successfully.",
                len(results),
            )

            return state

        except Exception as e:

            logger.exception("Retrieval Node failed.")

            state["retrieved_documents"] = []
            state["success"] = False
            state["error"] = str(e)

            return state