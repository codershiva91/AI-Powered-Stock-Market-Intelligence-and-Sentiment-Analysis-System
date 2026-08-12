"""
=========================================================
Context Builder Test
=========================================================
"""

from ai.retriever.retriever import Retriever
from ai.cross_encoder.reranker import CrossEncoderReranker
from ai.context_builder.builder import ContextBuilder
from ai.context_builder.formatter import ContextFormatter


def main():

    retriever = Retriever()

    reranker = CrossEncoderReranker()

    builder = ContextBuilder()

    print("=" * 100)
    print(" AI STOCK MARKET CONTEXT BUILDER ")
    print("=" * 100)

    query = input("\nEnter Query : ").strip()

    if not query:
        print("\nQuery cannot be empty.")
        return

    print("\nRetrieving documents...\n")

    retrieved_docs = retriever.search(
        query=query,
        top_k=10,
    )

    print(f"{len(retrieved_docs)} documents retrieved.")

    print("\nReranking documents...\n")

    reranked_docs = reranker.rerank(
        query=query,
        documents=retrieved_docs,
        top_k=5,
    )

    print(f"{len(reranked_docs)} documents after reranking.")

    print("\nBuilding context...\n")

    context = builder.build(reranked_docs)

    formatted = ContextFormatter.format(context)

    print(formatted)

    print("\n")
    print("=" * 100)
    print(" Context Builder Test Completed Successfully ")
    print("=" * 100)


if __name__ == "__main__":
    main()