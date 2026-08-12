"""
==============================================================================
Graph State Definition
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Shared state flowing through the LangGraph pipeline.

Each node reads from and writes to this state.

Workflow
--------
User Question
      │
      ▼
Query Analyzer
      ▼
Structured Data
      ▼
Recommendation
      ▼
Retriever
      ▼
Reranker
      ▼
Context Builder
      ▼
Prompt Builder
      ▼
Gemini
      ▼
Final Response

==============================================================================
"""

from typing import TypedDict, Dict, List, Any, Optional


class GraphState(TypedDict, total=False):
    """
    Shared state flowing through the LangGraph pipeline.
    """

    # -------------------------------------------------------------------------
    # User Input
    # -------------------------------------------------------------------------

    question: str

    # -------------------------------------------------------------------------
    # Query Analysis
    # -------------------------------------------------------------------------

    query_analysis: Dict[str, Any]

    # -------------------------------------------------------------------------
    # Structured Data
    # -------------------------------------------------------------------------

    stock_data: Dict[str, Any]

    technical_data: Dict[str, Any]

    fundamental_data: Dict[str, Any]

    sentiment_data: Dict[str, Any]

    # -------------------------------------------------------------------------
    # Recommendation Engine Output
    # -------------------------------------------------------------------------

    recommendation: Dict[str, Any]

    # -------------------------------------------------------------------------
    # Vector Retrieval
    # -------------------------------------------------------------------------

    retrieved_documents: List[Dict[str, Any]]

    reranked_documents: List[Dict[str, Any]]

    # -------------------------------------------------------------------------
    # LLM Context
    # -------------------------------------------------------------------------

    context: str

    prompt: str

    # -------------------------------------------------------------------------
    # Final Response
    # -------------------------------------------------------------------------

    response: str

    # -------------------------------------------------------------------------
    # Error Handling
    # -------------------------------------------------------------------------

    error: Optional[str]