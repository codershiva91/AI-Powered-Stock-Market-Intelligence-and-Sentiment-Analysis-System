"""
==============================================================================
Execution Plan
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Defines the execution strategy created by the Supervisor Agent.

==============================================================================
"""

from dataclasses import dataclass, field


@dataclass
class ExecutionPlan:
    """
    Supervisor execution strategy.
    """

    # ==========================================================
    # Original User Question
    # ==========================================================

    question: str

    # ==========================================================
    # User Objective
    # ==========================================================

    goal: str

    # ==========================================================
    # Selected Workflow
    # ==========================================================

    workflow: str

    # ==========================================================
    # Agents to Execute
    # ==========================================================

    agents: list[str] = field(default_factory=list)

    # ==========================================================
    # Planning Metadata
    # ==========================================================

    reasoning: str = ""

    confidence: float = 1.0

    priority: str = "NORMAL"

    # ==========================================================
    # Runtime Status
    # ==========================================================

    current_step: int = 0

    completed_steps: list[str] = field(default_factory=list)

    failed_steps: list[str] = field(default_factory=list)

    status: str = "PENDING"