"""
==============================================================================
Query Analyzer Logger
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Logging configuration for Query Analyzer
==============================================================================

"""

import logging
import os
from logging.handlers import RotatingFileHandler

from .config import LOGGER_NAME, LOG_LEVEL

# ==============================================================================
# LOG DIRECTORY
# ==============================================================================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(CURRENT_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "query_analyzer.log")

# ==============================================================================
# LOGGER
# ==============================================================================

logger = logging.getLogger(LOGGER_NAME)

if not logger.handlers:

    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter(

        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",

        datefmt="%Y-%m-%d %H:%M:%S"

    )

    # --------------------------------------------------------------------------
    # Console Handler
    # --------------------------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # --------------------------------------------------------------------------
    # File Handler
    # --------------------------------------------------------------------------

    file_handler = RotatingFileHandler(

        filename=LOG_FILE,

        maxBytes=5 * 1024 * 1024,      # 5 MB

        backupCount=5,

        encoding="utf-8"

    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.propagate = False


# ==============================================================================
# PUBLIC FUNCTION
# ==============================================================================

def get_logger(name: str = LOGGER_NAME):

    """
    Returns child logger.

    Example
    -------
    logger = get_logger(__name__)
    """

    return logger.getChild(name)