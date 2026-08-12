"""
==============================================================================
AI Backend Test Runner
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Standalone console application for validating the complete AI pipeline.

Validates
---------
✓ LangGraph Workflow
✓ MariaDB Connection
✓ Recommendation Engine
✓ Qdrant Retrieval
✓ Cross Encoder Reranker
✓ Context Builder
✓ Prompt Builder
✓ Gemini

==============================================================================
"""

import sys
import time
import traceback
from pathlib import Path

# =============================================================================
# Add Project Root to Python Path
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# =============================================================================
# Imports
# =============================================================================

from ai.langgraph.graph import graph
from ai.langgraph.state_factory import create_graph_state


# =============================================================================
# Main
# =============================================================================

def main():

    print("\n" + "=" * 80)
    print(" AI-Driven Stock Market Intelligence Platform ")
    print("=" * 80)

    print("\nType 'exit' to quit.\n")

    while True:

        question = input("Question > ").strip()

        if question.lower() in ["exit", "quit"]:

            print("\nGoodbye!\n")
            break

        if not question:

            print("Please enter a valid question.\n")
            continue

        try:

            # ----------------------------------------------------------
            # Create Initial State
            # ----------------------------------------------------------

            state = create_graph_state(question)

            print("\nRunning AI Pipeline...\n")

            start = time.perf_counter()

            # ----------------------------------------------------------
            # Execute LangGraph
            # ----------------------------------------------------------

            result = graph.invoke(state)

            elapsed = time.perf_counter() - start

            # ----------------------------------------------------------
            # Final Response
            # ----------------------------------------------------------

            print("\n" + "=" * 80)
            print("FINAL RESPONSE")
            print("=" * 80)

            print(result.get("response", "No response generated."))

            # ----------------------------------------------------------
            # Recommendation
            # ----------------------------------------------------------

            recommendation = result.get("recommendation", {})

            if recommendation:

                print("\n" + "=" * 80)
                print("RECOMMENDATION")
                print("=" * 80)

                print(
                    f"Recommendation : {recommendation.get('recommendation','N/A')}"
                )

                print(
                    f"Confidence     : {recommendation.get('confidence','N/A')}"
                )

                print(
                    f"Total Score    : {recommendation.get('total_score','N/A')}"
                )

            print("\nExecution Time : %.2f sec" % elapsed)

            print("=" * 80)

        except Exception as e:

            print("\n" + "=" * 80)
            print("PIPELINE FAILED")
            print("=" * 80)

            print(f"Error : {e}")

            print("\nDetailed Traceback:\n")

            traceback.print_exc()

            print("=" * 80)


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":

    main()