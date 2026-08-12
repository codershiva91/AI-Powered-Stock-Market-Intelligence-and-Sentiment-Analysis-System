"""
=========================================================
LLM Test
=========================================================
"""

from ai.llm.gemini_client import GeminiClient


def main():

    print("=" * 80)
    print(" GEMINI CLIENT TEST ")
    print("=" * 80)

    client = GeminiClient()

    question = input("\nEnter Question : ")

    response = client.generate(question)

    print("\n")
    print("=" * 80)
    print(" RESPONSE ")
    print("=" * 80)

    print(response)


if __name__ == "__main__":
    main()