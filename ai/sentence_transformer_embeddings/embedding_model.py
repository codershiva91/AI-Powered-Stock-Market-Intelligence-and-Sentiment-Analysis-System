"""
==============================================================================
Sentence Transformer Embedding Model
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Loads the Sentence Transformer model lazily (only when first required)
and provides helper functions for generating embeddings.

==============================================================================
"""

from sentence_transformers import SentenceTransformer
import numpy as np

from .config import (
    MODEL_NAME,
    DEVICE,
    NORMALIZE_EMBEDDINGS,
)

# ==============================================================================
# Global Model Instance
# ==============================================================================

_model = None


# ==============================================================================
# Load Model (Lazy Loading)
# ==============================================================================

def get_model():
    """
    Load the SentenceTransformer model only once.

    Returns
    -------
    SentenceTransformer
    """

    global _model

    if _model is None:

        print("=" * 60)
        print("Loading Sentence Transformer Model...")
        print(f"Model  : {MODEL_NAME}")
        print(f"Device : {DEVICE}")

        _model = SentenceTransformer(
            MODEL_NAME,
            device=DEVICE
        )

        print("Model Loaded Successfully")
        print("=" * 60)

    return _model


# ==============================================================================
# Generate Embedding for Single Text
# ==============================================================================

def generate_embedding(text: str):
    """
    Generate embedding for a single text.

    Parameters
    ----------
    text : str

    Returns
    -------
    list[float]
    """

    model = get_model()

    embedding = model.encode(
        text,
        normalize_embeddings=NORMALIZE_EMBEDDINGS,
        convert_to_numpy=True,
        show_progress_bar=False,
    )

    return embedding.tolist()


# ==============================================================================
# Generate Embeddings for Multiple Texts
# ==============================================================================

def generate_embeddings(texts, batch_size=32):
    """
    Generate embeddings for multiple texts.

    Parameters
    ----------
    texts : list[str]
    batch_size : int

    Returns
    -------
    list[list[float]]
    """

    model = get_model()

    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=NORMALIZE_EMBEDDINGS,
        convert_to_numpy=True,
        show_progress_bar=False,
    )

    return embeddings.tolist()


# ==============================================================================
# Get Embedding Dimension
# ==============================================================================

def get_embedding_dimension():
    """
    Return embedding dimension.

    Returns
    -------
    int
    """

    model = get_model()

    return model.get_sentence_embedding_dimension()


# ==============================================================================
# Cosine Similarity
# ==============================================================================

def cosine_similarity(vector1, vector2):
    """
    Compute cosine similarity between two vectors.

    Parameters
    ----------
    vector1 : list
    vector2 : list

    Returns
    -------
    float
    """

    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    denominator = np.linalg.norm(vector1) * np.linalg.norm(vector2)

    if denominator == 0:
        return 0.0

    similarity = np.dot(vector1, vector2) / denominator

    return float(similarity)