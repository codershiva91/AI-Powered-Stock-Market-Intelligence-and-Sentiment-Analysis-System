"""
==============================================================================
Graph State Factory
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Factory for creating the initial GraphState used by the LangGraph workflow.

Every AI Agent should use this factory instead of manually creating the
GraphState dictionary.

==============================================================================

"""

"""
State Factory
Creates the initial GraphState.
"""

from ai.langgraph.state import GraphState


def create_graph_state(question: str) -> GraphState:

    return GraphState(

        question=question,

        query_analysis={},

        stock_data={},

        technical_data={},

        fundamental_data={},

        retrieved_documents=[],

        reranked_documents=[],

        context="",

        prompt="",

        response="",

        error=None
    )