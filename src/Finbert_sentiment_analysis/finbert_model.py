"""
==========================================================
FinBERT Model Module

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Loads the FinBERT model once and provides a reusable
function for sentiment prediction.
==========================================================
"""

from transformers import pipeline

from config import (
    MODEL_NAME,
    MAX_TEXT_LENGTH
)

from logger import get_logger

logger = get_logger()

# ---------------------------------------------------------
# Load FinBERT Model
# ---------------------------------------------------------

logger.info("Loading FinBERT model...")

classifier = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME
)

logger.info("FinBERT model loaded successfully.")


# ---------------------------------------------------------
# Sentiment Prediction Function
# ---------------------------------------------------------

def predict_sentiment(text):
    """
    Predict sentiment using FinBERT.

    Parameters
    ----------
    text : str
        News article text.

    Returns
    -------
    dict
        {
            "label": "Positive" | "Negative" | "Neutral",
            "score": float
        }
    """

    result = classifier(
        text,
        truncation=True,
        max_length=MAX_TEXT_LENGTH
    )[0]

    # Normalize label returned by FinBERT
    label = result["label"].strip().lower()

    label_mapping = {
        "positive": "Positive",
        "negative": "Negative",
        "neutral": "Neutral",
        "label_0": "Positive",
        "label_1": "Negative",
        "label_2": "Neutral",
    }

    if label not in label_mapping:
        raise ValueError(f"Unknown FinBERT label: {result['label']}")

    return {
        "label": label_mapping[label],
        "score": float(result["score"])
    }