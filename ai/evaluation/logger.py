"""
=========================================================
Evaluation Logger
=========================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Central logger for the Evaluation module.

Responsibilities
----------------
1. Configure logging
2. Create reusable logger
3. Prevent duplicate handlers
4. Standardize log format

=========================================================
"""

import logging

from ai.evaluation.config import LOG_LEVEL


# =====================================================
# Logger Factory
# =====================================================

def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL.upper()))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.propagate = False

    return logger