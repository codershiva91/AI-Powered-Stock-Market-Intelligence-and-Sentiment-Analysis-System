# # """
# # Test Semantic Search in Qdrant
# # """

# # from embedding_model import generate_embedding
# # from qdrant_manager import QdrantManager


# # def main():

# #     print("=" * 70)
# #     print("Testing Semantic Search")
# #     print("=" * 70)

# #     # Connect to Qdrant
# #     qdrant = QdrantManager()

# #     # Search Query
# #     query = "Reliance Industries quarterly profit"

# #     print(f"\nQuery : {query}")

# #     # Generate embedding
# #     query_vector = generate_embedding(query)

# #     print("Embedding Generated Successfully")

# #     # Search Qdrant
# #     results = qdrant.search(query_vector, limit=5)

# #     print("\nTop 5 Similar News")
# #     print("=" * 100)

# #     if not results:
# #         print("No Results Found")
# #         return

# #     for i, result in enumerate(results, start=1):

# #         payload = result.payload

# #         print(f"\nResult {i}")
# #         print("-" * 100)

# #         print("News ID      :", payload.get("news_id"))
# #         print("Title        :", payload.get("title"))
# #         print("Source       :", payload.get("source"))
# #         print("Topic        :", payload.get("topic"))
# #         print("News Type    :", payload.get("news_type"))
# #         print("Sentiment    :", payload.get("sentiment"))
# #         print("Confidence   :", payload.get("confidence_score"))
# #         print("Published At :", payload.get("published_at"))
# #         print("Similarity   :", round(result.score, 4))

# #     print("\n" + "=" * 100)
# #     print("Semantic Search Test Completed")
# #     print("=" * 100)


# # if __name__ == "__main__":
# #     main()


# from embedding_model import generate_embedding
# from qdrant_manager import QdrantManager


# def main():

#     qdrant = QdrantManager()

#     query = "Reliance Industries quarterly profit"

#     print(f"\nQuery : {query}")

#     query_vector = generate_embedding(query)

#     results = qdrant.search(query_vector, limit=5)

#     print("\nTop Results")
#     print("=" * 80)

#     for i, result in enumerate(results, 1):

#         payload = result.payload

#         print(f"\nResult {i}")
#         print("-" * 80)
#         print("News ID :", payload.get("news_id"))
#         print("Title   :", payload.get("title"))
#         print("Source  :", payload.get("source"))
#         print("Topic   :", payload.get("topic"))
#         print("Score   :", round(result.score, 4))


# if __name__ == "__main__":
#     main()

from embedding_model import generate_embedding
from qdrant_manager import QdrantManager

qdrant = QdrantManager()

query = "Reliance Industries quarterly profit"

embedding = generate_embedding(query)

results = qdrant.search(embedding)

print("=" * 80)

for r in results:

    print(r.score)

    print(r.payload)

    print("-" * 80)