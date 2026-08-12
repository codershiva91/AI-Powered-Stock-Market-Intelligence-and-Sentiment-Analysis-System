"""
Logging configuration for the Sentence Transformer Embedding module.
"""

import logging
import os

from .config import LOG_DIRECTORY, LOG_FILE, LOG_LEVEL


def get_logger(name: str = "SentenceTransformer") -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    # Create log directory if it doesn't exist
    os.makedirs(LOG_DIRECTORY, exist_ok=True)

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL.upper()))

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # -----------------------------
    # Console Handler
    # -----------------------------
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # -----------------------------
    # File Handler
    # -----------------------------
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

