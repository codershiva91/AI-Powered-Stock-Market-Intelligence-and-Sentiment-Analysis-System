"""
==============================================================================
Workflow Router
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Routes the user's request to the appropriate workflow based on the
intent detected by the Query Analyzer.

Responsibilities
----------------
- Read intent from GraphState
- Select the correct workflow
- Return the next workflow name

The router does NOT:
- Query MariaDB
- Query Qdrant
- Call Gemini
- Perform business logic

==============================================================================
"""

from ai.langgraph.state import GraphState


class WorkflowRouter:
    """
    Determines which workflow should execute next.
    """

    def route(self, state: GraphState) -> str:
        """
        Route based on detected intent.

        Returns
        -------
        str
            Workflow name
        """

        query_analysis = state.get("query_analysis", {})
        intent = query_analysis.get("intent", "GENERAL_QUERY")

        routes = {

            "BUY_SELL_RECOMMENDATION": "company_workflow",

            "COMPANY_ANALYSIS": "company_workflow",

            "COMPANY_COMPARISON": "company_workflow",

            "MARKET_ANALYSIS": "market_workflow",

            "NEWS_ANALYSIS": "news_workflow",

            "PORTFOLIO_ANALYSIS": "portfolio_workflow",

            "GENERAL_QUERY": "general_workflow"

        }

        return routes.get(intent, "general_workflow")