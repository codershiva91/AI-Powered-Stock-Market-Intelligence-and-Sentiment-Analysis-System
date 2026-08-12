from database import fetch_news_batch

from embedding_service import EmbeddingService


service = EmbeddingService()

rows = fetch_news_batch(0, 1)

point = service.process_news(rows[0])

print(point)