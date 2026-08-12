# from logger import get_logger

# logger = get_logger()

# logger.info("Embedding ETL Started")

# logger.warning("This is a warning")

# logger.error("This is an error")

# from preprocess import prepare_document

# title = "Reliance Stock Gains"

# article = """
# Reliance shares jumped 5% today.

# Read more:
# https://moneycontrol.com/news/123
# """

# doc = prepare_document(title, article)

# print(doc)


# from embedding_model import (
#     generate_embedding,
#     get_embedding_dimension,
# )

# text = """
# Reliance Industries reported strong quarterly earnings.
# """

# embedding = generate_embedding(text)

# print(f"Embedding Dimension : {len(embedding)}")
# print(f"Model Dimension     : {get_embedding_dimension()}")

# print("\nFirst 10 Values:")
# print(embedding[:10])   


from qdrant_manager import QdrantManager

db = QdrantManager()

db.create_collection()

print(db.collection_info())

print("Total vectors :", db.count_vectors())