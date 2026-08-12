"""
==============================================================
Supervisor Test Runner
==============================================================
"""

import sys
from pathlib import Path

# ------------------------------------------------------------
# Add Project Root to Python Path
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

# ------------------------------------------------------------

from ai.agents.supervisor.supervisor import SupervisorAgent


def main():

    supervisor = SupervisorAgent()

    print("=" * 70)
    print("AI Supervisor Test")
    print("=" * 70)

    while True:

        question = input("\nQuestion > ").strip()

        if question.lower() in ["exit", "quit"]:
            break

        response = supervisor.answer(question)

        print("\n" + "=" * 70)
        print("FINAL RESPONSE")
        print("=" * 70)
        print(response)


if __name__ == "__main__":

    main()