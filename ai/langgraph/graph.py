"""
==============================================================================
LangGraph Workflow
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Main LangGraph workflow for the AI-powered Stock Market Intelligence System.

Pipeline
--------
User Question
      │
      ▼
Query Analyzer
      ▼
Structured Data Node
      ▼
Recommendation Node
      ▼
Retriever
      ▼
Cross Encoder Reranker
      ▼
Context Builder
      ▼
Prompt Builder
      ▼
Gemini
      ▼
Final Answer

==============================================================================
"""

from langgraph.graph import StateGraph, END

from ai.langgraph.state import GraphState

from ai.langgraph.query_analyzer_node import QueryAnalyzerNode
from ai.langgraph.structured_data_node import StructuredDataNode
from ai.langgraph.recommendation_node import RecommendationNode
from ai.langgraph.retrieval_node import RetrievalNode
from ai.langgraph.reranker_node import RerankerNode
from ai.langgraph.context_builder_node import ContextBuilderNode
from ai.langgraph.prompt_builder_node import PromptBuilderNode
from ai.langgraph.gemini_node import GeminiNode


# =============================================================================
# Build Graph
# =============================================================================

def build_graph():
    """
    Build and compile the LangGraph workflow.
    """

    builder = StateGraph(GraphState)

    # -------------------------------------------------------------------------
    # Register Nodes
    # -------------------------------------------------------------------------

    builder.add_node(
        "query_analyzer",
        QueryAnalyzerNode()
    )

    builder.add_node(
        "structured_data",
        StructuredDataNode()
    )

    builder.add_node(
        "recommendation",
        RecommendationNode()
    )

    builder.add_node(
        "retriever",
        RetrievalNode()
    )

    builder.add_node(
        "reranker",
        RerankerNode()
    )

    builder.add_node(
        "context_builder",
        ContextBuilderNode()
    )

    builder.add_node(
        "prompt_builder",
        PromptBuilderNode()
    )

    builder.add_node(
        "gemini",
        GeminiNode()
    )

    # -------------------------------------------------------------------------
    # Entry Point
    # -------------------------------------------------------------------------

    builder.set_entry_point("query_analyzer")

    # -------------------------------------------------------------------------
    # Workflow
    # -------------------------------------------------------------------------

    builder.add_edge(
        "query_analyzer",
        "structured_data"
    )

    builder.add_edge(
        "structured_data",
        "recommendation"
    )

    builder.add_edge(
        "recommendation",
        "retriever"
    )

    builder.add_edge(
        "retriever",
        "reranker"
    )

    builder.add_edge(
        "reranker",
        "context_builder"
    )

    builder.add_edge(
        "context_builder",
        "prompt_builder"
    )

    builder.add_edge(
        "prompt_builder",
        "gemini"
    )

    builder.add_edge(
        "gemini",
        END
    )

    return builder.compile()


# =============================================================================
# Compile Graph
# =============================================================================

graph = build_graph()


# =============================================================================
# Local Testing
# =============================================================================

if __name__ == "__main__":

    initial_state = {

        # -------------------------------------------------------------
        # User Question
        # -------------------------------------------------------------

        "question": "Should I invest in Reliance Industries?",

        # -------------------------------------------------------------
        # Query Analysis
        # -------------------------------------------------------------

        "query_analysis": {},

        # -------------------------------------------------------------
        # Structured Data
        # -------------------------------------------------------------

        "stock_data": {},

        "technical_data": {},

        "fundamental_data": {},

        "sentiment_data": {},

        # -------------------------------------------------------------
        # Recommendation
        # -------------------------------------------------------------

        "recommendation": {},

        # -------------------------------------------------------------
        # Retrieval
        # -------------------------------------------------------------

        "retrieved_documents": [],

        "reranked_documents": [],

        # -------------------------------------------------------------
        # Prompt Building
        # -------------------------------------------------------------

        "context": "",

        "prompt": "",

        # -------------------------------------------------------------
        # Final Response
        # -------------------------------------------------------------

        "response": "",

        # -------------------------------------------------------------
        # Error
        # -------------------------------------------------------------

        "error": None,
    }

    result = graph.invoke(initial_state)

    print("\n" + "=" * 80)
    print("FINAL RESPONSE")
    print("=" * 80)
    print(result["response"])