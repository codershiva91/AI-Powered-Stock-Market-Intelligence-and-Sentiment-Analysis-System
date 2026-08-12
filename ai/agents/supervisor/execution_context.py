"""
==============================================================================
Execution Context
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Shared execution context used by the Supervisor Agent and all specialized
agents during a single AI request.

Every agent reads from and writes to this context.

==============================================================================

"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:
    """
    Shared context for one AI request.
    """

    # ==========================================================
    # User Request
    # ==========================================================

    question: str

    # ==========================================================
    # Query Analysis
    # ==========================================================

    query_analysis: dict = field(default_factory=dict)

    # ==========================================================
    # Structured Data
    # ==========================================================

    stock_data: dict = field(default_factory=dict)

    technical_data: dict = field(default_factory=dict)

    fundamental_data: dict = field(default_factory=dict)

    sentiment_data: dict = field(default_factory=dict)

    # ==========================================================
    # Recommendation
    # ==========================================================

    recommendation: dict = field(default_factory=dict)

    # ==========================================================
    # Retrieval
    # ==========================================================

    retrieved_documents: list[dict] = field(default_factory=list)

    reranked_documents: list[dict] = field(default_factory=list)

    # ==========================================================
    # Context
    # ==========================================================

    context: str = ""

    prompt: str = ""

    response: str = ""

    # ==========================================================
    # Execution
    # ==========================================================

    execution_plan: Any = None

    current_agent: str = ""

    completed_agents: list[str] = field(default_factory=list)

    execution_logs: list[str] = field(default_factory=list)

    # ==========================================================
    # Errors
    # ==========================================================

    error: str | None = None