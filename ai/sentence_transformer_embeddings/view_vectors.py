from qdrant_manager import QdrantManager

q = QdrantManager()

points, _ = q.client.scroll(
    collection_name="news_embeddings",
    limit=5,
    with_payload=True,
    with_vectors=True
)

for point in points:
    print("=" * 60)
    print("ID:", point.id)
    print("Payload:", point.payload)
    print("Vector dimension:", len(point.vector))
    print("First 10 values:", point.vector[:10])