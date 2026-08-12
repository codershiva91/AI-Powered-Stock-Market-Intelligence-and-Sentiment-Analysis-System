"""
==============================================================================
LangGraph Gemini Node
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
LangGraph node responsible for generating the final answer
using the Gemini Large Language Model.

Responsibilities
----------------
1. Read prompt from GraphState
2. Validate prompt
3. Send prompt to Gemini
4. Store generated response
5. Handle API errors
6. Log execution details

==============================================================================
"""

from ai.langgraph.state import GraphState

from ai.llm.gemini import GeminiClient
from ai.llm.logger import get_logger

logger = get_logger(__name__)


class GeminiNode:
    """
    LangGraph node responsible for
    generating the final response.
    """

    ##################################################################

    def __init__(self):

        self.llm = GeminiClient()

    ##################################################################

    def __call__(self, state: GraphState) -> GraphState:

        try:

            logger.info("=" * 60)
            logger.info("GEMINI NODE")
            logger.info("=" * 60)

            prompt = state.get("prompt", "").strip()

            if not prompt:

                logger.error("Prompt is empty.")

                state["response"] = ""
                state["success"] = False
                state["error"] = "Prompt cannot be empty."

                return state

            logger.info("Sending prompt to Gemini...")

            response = self.llm.generate(prompt)

            state["response"] = response
            state["success"] = True
            state["error"] = None

            logger.info(
                "Gemini generated response successfully (%d characters).",
                len(response),
            )

            return state

        except Exception as e:

            logger.exception("Gemini Node failed.")

            state["response"] = ""
            state["success"] = False
            state["error"] = str(e)

            return state