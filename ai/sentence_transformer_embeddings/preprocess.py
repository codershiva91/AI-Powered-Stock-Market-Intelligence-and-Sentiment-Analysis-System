"""
Text preprocessing for the Sentence Transformer Embedding module.
"""

import re
from html import unescape


def clean_text(text: str) -> str:
    """
    Clean text before generating embeddings.

    The goal is to remove unwanted noise while preserving
    the semantic meaning of the text.

    Parameters
    ----------
    text : str
        Raw news article text.

    Returns
    -------
    str
        Cleaned text.
    """

    # Handle None values
    if text is None:
        return ""

    # Convert to string
    text = str(text)

    # Decode HTML entities
    text = unescape(text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Replace newlines and tabs
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text


def prepare_document(title: str, article: str) -> str:
    """
    Combine title and article into one document.

    Parameters
    ----------
    title : str
    article : str

    Returns
    -------
    str
        Combined document.
    """

    title = clean_text(title)
    article = clean_text(article)

    if title and article:
        return f"{title}. {article}"

    if title:
        return title

    if article:
        return article

    return ""


def is_valid_document(document: str, min_length: int = 30) -> bool:
    """
    Check whether a document is suitable for embedding.

    Parameters
    ----------
    document : str
    min_length : int

    Returns
    -------
    bool
    """

    if not document:
        return False

    if len(document.strip()) < min_length:
        return False

    return True