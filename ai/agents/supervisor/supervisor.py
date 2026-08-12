"""
==============================================================================
AI Supervisor Agent
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform

Description
-----------
Central orchestration agent for the AI-Driven Stock Market Intelligence
Platform.

Responsibilities
----------------
1. Receive user question
2. Run Query Analyzer
3. Create Execution Plan
4. Delegate execution to Dispatcher
5. Return final AI response

==============================================================================
"""

from ai.query_analyzer.analyzer import QueryAnalyzer

from ai.agents.supervisor.planner import Planner
from ai.agents.supervisor.dispatcher import Dispatcher

from ai.common.logger import get_logger
from ai.common.exceptions import AgentError

logger = get_logger(__name__)


class SupervisorAgent:
    """
    Central AI Orchestrator.
    """

    ##################################################################

    def __init__(self):

        logger.info("Initializing Supervisor Agent...")

        self.query_analyzer = QueryAnalyzer()

        self.planner = Planner()

        self.dispatcher = Dispatcher()

        logger.info("Supervisor Agent initialized successfully.")

    ##################################################################
    # Main Entry Point
    ##################################################################

    def answer(self, question: str) -> str:
        """
        Execute complete AI workflow.

        Parameters
        ----------
        question : str

        Returns
        -------
        str
            Final AI response.
        """

        logger.info("=" * 80)
        logger.info("SUPERVISOR AGENT")
        logger.info("=" * 80)

        logger.info("User Question : %s", question)

        try:

            # ==========================================================
            # Step 1 : Query Analysis
            # ==========================================================

            logger.info("Running Query Analyzer...")

            query_analysis = self.query_analyzer.analyze(question)

            logger.info(
                "Intent : %s",
                query_analysis.get("intent")
            )

            logger.info(
                "Confidence : %s",
                query_analysis.get("confidence")
            )

            # ==========================================================
            # Step 2 : Execution Planning
            # ==========================================================

            logger.info("Creating Execution Plan...")

            execution_plan = self.planner.create_plan(
                question=question,
                query_analysis=query_analysis,
            )

            logger.info("=" * 80)
            logger.info("EXECUTION PLAN")
            logger.info("=" * 80)

            logger.info(
                "Question : %s",
                execution_plan.question
            )

            logger.info(
                "Workflow : %s",
                execution_plan.workflow
            )

            logger.info(
                "Goal : %s",
                execution_plan.goal
            )

            logger.info(
                "Agents : %s",
                execution_plan.agents
            )

            logger.info(
                "Priority : %s",
                execution_plan.priority
            )

            logger.info(
                "Confidence : %.2f",
                execution_plan.confidence
            )

            # ==========================================================
            # Step 3 : Dispatch
            # ==========================================================

            logger.info("Delegating to Dispatcher...")

            response = self.dispatcher.execute(
                execution_plan
            )

            logger.info("Supervisor completed successfully.")

            return response

        except Exception as e:

            logger.exception(
                "Supervisor execution failed."
            )

            raise AgentError(
                f"Supervisor Error : {str(e)}"
            ) from e