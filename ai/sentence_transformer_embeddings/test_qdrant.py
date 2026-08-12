# from qdrant_manager import QdrantManager

# db = QdrantManager()

# db.create_collection()

# print(db.collection_info())
# print(db.count_vectors())

from qdrant_manager import QdrantManager

q = QdrantManager()

count = q.count_vectors()

print(f"Total vectors in Qdrant: {count}")