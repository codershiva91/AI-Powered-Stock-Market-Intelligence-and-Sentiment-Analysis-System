"""
=========================================================
Retriever Test Script
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Tests the Semantic Retriever module.

=========================================================
"""

from ai.retriever.retriever import Retriever


def print_result(result: dict, index: int):

    print("\n" + "=" * 100)

    print(f"Result #{index}")

    print("=" * 100)

    print(f"Similarity Score : {result['score']}")
    print(f"News ID          : {result['news_id']}")
    print(f"Title            : {result['title']}")
    print(f"Topic            : {result['topic']}")
    print(f"Source           : {result['source']}")
    print(f"News Type        : {result['news_type']}")
    print(f"Sentiment        : {result['sentiment']}")
    print(f"Confidence Score : {result['confidence_score']}")
    print(f"Published At     : {result['published_at']}")

    print("\nDocument Preview")
    print("-" * 100)

    document = result.get("document") or ""

    if len(document) > 400:
        document = document[:400] + "..."

    print(document)


def main():

    retriever = Retriever()

    print("\n")
    print("=" * 100)
    print(" AI STOCK MARKET INTELLIGENCE RETRIEVER ")
    print("=" * 100)

    query = input("\nEnter Search Query : ").strip()

    if not query:

        print("\nQuery cannot be empty.")
        return

    print("\nOptional Filters (Press Enter to Skip)\n")

    topic = input("Topic : ").strip() or None
    sentiment = input("Sentiment (Positive/Negative/Neutral): ").strip() or None
    news_type = input("News Type (MARKET/COMPANY/SECTOR/INDEX/GENERAL): ").strip() or None
    source = input("Source : ").strip() or None

    print("\nSearching...\n")

    try:

        results = retriever.search(
            query=query,
            topic=topic,
            sentiment=sentiment,
            news_type=news_type,
            source=source,
        )

        print(f"\nRetrieved {len(results)} document(s).\n")

        if not results:

            print("No matching documents found.")
            return

        for idx, result in enumerate(results, start=1):

            print_result(result, idx)

        print("\n")
        print("=" * 100)
        print("Retrieval Completed Successfully")
        print("=" * 100)

    except Exception as e:

        print("\nRetriever Error")
        print("-" * 100)
        print(e)


if __name__ == "__main__":
    main()