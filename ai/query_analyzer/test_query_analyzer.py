"""
==============================================================================
Query Analyzer Test
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Test suite for Query Analyzer V2
==============================================================================
"""

from pprint import pprint

from .analyzer import QueryAnalyzer


TEST_QUERIES = [

    # ---------------------------------------------------------
    # Company News
    # ---------------------------------------------------------

    "Latest news about Reliance",

    "Show latest news of Infosys",

    "Recent updates on TCS",

    "News about HDFC Bank today",

    # ---------------------------------------------------------
    # Company Comparison
    # ---------------------------------------------------------

    "Compare Reliance and Infosys",

    "Compare TCS vs Wipro",

    "Difference between HDFC Bank and ICICI Bank",

    "Which is better Infosys or TCS?",

    # ---------------------------------------------------------
    # Market Analysis
    # ---------------------------------------------------------

    "Why did NIFTY fall today?",

    "How is Sensex performing?",

    "Market trend this week",

    "Bank Nifty movement",

    # ---------------------------------------------------------
    # Sector Analysis
    # ---------------------------------------------------------

    "Banking sector analysis",

    "IT sector performance",

    "Auto sector latest news",

    "Pharma stocks",

    # ---------------------------------------------------------
    # Sentiment
    # ---------------------------------------------------------

    "Positive news about Reliance",

    "Negative news about Adani",

    "Bullish on Infosys",

    "Bearish on Tata Motors",

    # ---------------------------------------------------------
    # Time Filters
    # ---------------------------------------------------------

    "Infosys news yesterday",

    "Reliance news this week",

    "TCS news last month",

    "Nifty this year",

    # ---------------------------------------------------------
    # General Queries
    # ---------------------------------------------------------

    "Best stock to buy",

    "Should I invest now?",

    "What is stock market?",

    # ---------------------------------------------------------
    # Edge Cases
    # ---------------------------------------------------------

    "",

    "     ",

    None

]


def main():

    analyzer = QueryAnalyzer()

    print("=" * 90)
    print("QUERY ANALYZER TEST SUITE")
    print("=" * 90)

    passed = 0
    failed = 0

    for index, query in enumerate(TEST_QUERIES, start=1):

        print("\n")
        print("=" * 90)

        print(f"TEST #{index}")

        print("-" * 90)

        print("Query :")

        print(query)

        print("-" * 90)

        try:

            result = analyzer.analyze(query)

            pprint(result)

            passed += 1

            print("\nStatus : PASS")

        except Exception as e:

            failed += 1

            print("\nStatus : FAIL")

            print(e)

    print("\n")
    print("=" * 90)

    print("SUMMARY")

    print("=" * 90)

    print(f"Passed : {passed}")

    print(f"Failed : {failed}")

    print(f"Total  : {len(TEST_QUERIES)}")

    print("=" * 90)


if __name__ == "__main__":
    main()