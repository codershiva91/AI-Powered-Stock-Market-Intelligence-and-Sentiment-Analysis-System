"""
==========================================================
Text Preprocessing Module

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Cleans raw news article text before sentiment analysis.

Features
--------
✓ Remove HTML Tags
✓ Remove URLs
✓ Remove Newlines and Tabs
✓ Normalize Whitespace
==========================================================
"""

import re


def clean_text(text):
    """
    Clean news article text before sentiment analysis.

    Parameters
    ----------
    text : str

    Returns
    -------
    str
        Cleaned text.
    """

    if not text:
        return ""

    # Convert to string
    text = str(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Replace newlines and tabs
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()