from ai.prompt_builder.builder import PromptBuilder
from ai.prompt_builder.formatter import PromptFormatter

def main():

    builder = PromptBuilder()

    # Simulated Query Analyzer Output
    query_analysis = {

        "intent": "STOCK_SENTIMENT",

        "company_names": ["Reliance Industries"],

        "company_symbols": ["RELIANCE.NS"],

        "sector": None,

        "market_index": None,

        "sentiment": "POSITIVE",

        "time_filter": "THIS_WEEK",

        "confidence": 0.92

    }

    # Dummy Context
    context = """
Reliance Industries reported strong quarterly earnings.

Several brokerages upgraded the stock.

The overall sentiment remained positive.

Source: Moneycontrol
"""

    question = "Positive news about Reliance this week"

    prompt = builder.build(
        question=question,
        context=context,
        query_analysis=query_analysis
    )

    print(PromptFormatter.format(prompt))


if __name__ == "__main__":
    main()