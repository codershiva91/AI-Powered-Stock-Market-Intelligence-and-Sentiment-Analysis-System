from ai.sentence_transformer_embeddings.qdrant_manager import QdrantManager


manager = QdrantManager()

points = manager.get_all_points()

print(f"Total Points : {len(points)}")

if points:
    print("\nFirst Payload:\n")
    print(points[0].payload)
else:
    print("No points found in the collection.")