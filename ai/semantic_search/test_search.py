"""
test_search.py
==============

Test script for Semantic Search.

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence System
"""

from .semantic_search import SemanticSearch
from .formatter import SearchResultFormatter
from .filters import SearchFilters
from .exceptions import (
    EmptyQueryError,
    EmbeddingGenerationError,
    QdrantSearchError,
)

def main():

    print("=" * 70)
    print("AI Stock Market Semantic Search")
    print("=" * 70)

    search_engine = SemanticSearch()

    while True:

        query = input("\nEnter your search query (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        try:

            results = search_engine.search(
                query=query,
                top_k=5
            )

            # Example filter (optional)
            # results = SearchFilters.filter_results(
            #     results,
            #     sentiment="Positive"
            # )

            output = SearchResultFormatter.format_console(results)

            print(output)

        except EmptyQueryError as e:
            print(f"\nError: {e}")

        except EmbeddingGenerationError as e:
            print(f"\nEmbedding Error: {e}")

        except QdrantSearchError as e:
            print(f"\nSearch Error: {e}")

        except Exception as e:
            print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()