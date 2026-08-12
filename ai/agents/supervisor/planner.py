"""
==============================================================================
Planner
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Creates an ExecutionPlan from the Query Analyzer output.

Responsibilities
----------------
1. Read original user question
2. Read Query Analysis
3. Determine execution strategy
4. Build ExecutionPlan
5. Return ExecutionPlan

==============================================================================
"""

from ai.agents.supervisor.execution_plan import ExecutionPlan
from ai.agents.supervisor.planner_config import PLANNER_RULES


class Planner:
    """
    Converts Query Analysis into an Execution Plan.
    """

    def create_plan(
        self,
        question: str,
        query_analysis: dict,
    ) -> ExecutionPlan:
        """
        Create an execution plan.

        Parameters
        ----------
        question : str
            Original user question.

        query_analysis : dict
            Output from Query Analyzer.

        Returns
        -------
        ExecutionPlan
        """

        # ---------------------------------------------------------
        # Extract Query Information
        # ---------------------------------------------------------

        intent = query_analysis.get(
            "intent",
            "GENERAL_QUERY"
        )

        confidence = query_analysis.get(
            "confidence",
            1.0
        )

        # ---------------------------------------------------------
        # Lookup Planning Rules
        # ---------------------------------------------------------

        rule = PLANNER_RULES.get(
            intent,
            PLANNER_RULES["GENERAL_QUERY"]
        )

        # ---------------------------------------------------------
        # Build Execution Plan
        # ---------------------------------------------------------

        return ExecutionPlan(

            question=question,

            goal=rule["goal"],

            workflow=rule["workflow"],

            agents=rule["agents"],

            confidence=confidence,

            priority=rule["priority"],

            reasoning=f"Execution plan generated for intent '{intent}'"

        )