from ai.sentence_transformer_embeddings.qdrant_manager import QdrantManager

qdrant = QdrantManager()

qdrant.create_collection()

print("Collection Created Successfully")