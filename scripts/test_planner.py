"""
Planner Test
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

from ai.query_analyzer.analyzer import QueryAnalyzer
from ai.agents.supervisor.planner import Planner


def main():

    analyzer = QueryAnalyzer()

    planner = Planner()

    while True:

        question = input("\nQuestion > ")

        if question.lower() == "exit":
            break

        analysis = analyzer.analyze(question)

        plan = planner.create_plan(analysis)

        print("\n" + "=" * 60)

        print("EXECUTION PLAN")

        print("=" * 60)

        print(f"Goal       : {plan.goal}")

        print(f"Workflow   : {plan.workflow}")

        print(f"Priority   : {plan.priority}")

        print(f"Confidence : {plan.confidence}")

        print("\nAgents")

        for agent in plan.agents:

            print(f"   ✓ {agent}")

        print("\nReasoning")

        print(plan.reasoning)


if __name__ == "__main__":

    main()