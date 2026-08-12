"""
==============================================================================
LangGraph V2

Workflow Orchestrator

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
==============================================================================

Architecture

User
 │
 ▼
Query Analyzer
 │
 ▼
Workflow Router
 │
 ├── Company Workflow
 ├── News Workflow
 ├── Market Workflow
 └── Portfolio Workflow

==============================================================================
"""

from ai.langgraph.query_analyzer_node import QueryAnalyzerNode
from ai.langgraph.router import WorkflowRouter

from ai.langgraph.workflows.company_workflow import company_workflow
from ai.langgraph.workflows.news_workflow import news_workflow


class GraphV2:

    def __init__(self):

        self.query_node = QueryAnalyzerNode()

        self.router = WorkflowRouter()

    def invoke(self, state):

        # Step 1
        state = self.query_node(state)

        # Step 2
        workflow = self.router.route(state)

        # Step 3
        if workflow == "company_workflow":

            return company_workflow.invoke(state)

        elif workflow == "news_workflow":

            return news_workflow.invoke(state)

        else:

            raise NotImplementedError(
                f"Workflow '{workflow}' not implemented."
            )


graph_v2 = GraphV2()