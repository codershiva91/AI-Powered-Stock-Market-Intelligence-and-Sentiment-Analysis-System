from qdrant_manager import QdrantManager

q = QdrantManager()

print("=" * 50)
print("Total vectors in Qdrant:")
print(q.count_vectors())
print("=" * 50)