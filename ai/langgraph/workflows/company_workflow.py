"""
==============================================================================
Company Workflow
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Workflow for company analysis and investment recommendation.

Handles:

• Buy/Sell Recommendation
• Company Analysis
• Stock Analysis
• Long-term Investment Queries

==============================================================================
"""

from langgraph.graph import StateGraph, END

from ai.langgraph.state import GraphState

from ai.langgraph.structured_data_node import StructuredDataNode
from ai.langgraph.recommendation_node import RecommendationNode
from ai.langgraph.retrieval_node import RetrievalNode
from ai.langgraph.reranker_node import RerankerNode
from ai.langgraph.context_builder_node import ContextBuilderNode
from ai.langgraph.prompt_builder_node import PromptBuilderNode
from ai.langgraph.gemini_node import GeminiNode


def build_company_workflow():

    builder = StateGraph(GraphState)

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

    builder.set_entry_point("structured_data")

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


company_workflow = build_company_workflow()