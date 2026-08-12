"""
==============================================================================
News Workflow
==============================================================================

Handles News Analysis Only.
==============================================================================
"""

from langgraph.graph import StateGraph, END

from ai.langgraph.state import GraphState

from ai.langgraph.retrieval_node import RetrievalNode
from ai.langgraph.reranker_node import RerankerNode
from ai.langgraph.context_builder_node import ContextBuilderNode
from ai.langgraph.prompt_builder_node import PromptBuilderNode
from ai.langgraph.gemini_node import GeminiNode


def build_news_workflow():

    builder = StateGraph(GraphState)

    builder.add_node("retriever", RetrievalNode())
    builder.add_node("reranker", RerankerNode())
    builder.add_node("context_builder", ContextBuilderNode())
    builder.add_node("prompt_builder", PromptBuilderNode())
    builder.add_node("gemini", GeminiNode())

    builder.set_entry_point("retriever")

    builder.add_edge("retriever", "reranker")
    builder.add_edge("reranker", "context_builder")
    builder.add_edge("context_builder", "prompt_builder")
    builder.add_edge("prompt_builder", "gemini")
    builder.add_edge("gemini", END)

    return builder.compile()


news_workflow = build_news_workflow()