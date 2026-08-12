"""
=========================================================
Cross Encoder Model Loader
=========================================================

Loads the Cross Encoder model once and reuses it
throughout the application.
"""

from sentence_transformers import CrossEncoder

from .config import MODEL_NAME

print("=" * 60)
print("Loading Cross Encoder Model...")
print(f"Model : {MODEL_NAME}")

cross_encoder = CrossEncoder(MODEL_NAME)

print("Cross Encoder Loaded Successfully")
print("=" * 60)