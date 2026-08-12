# """
# logger.py
# Production logger
# """

# import logging
# import os

# from config import LOG_DIR
# from config import LOG_FILE


# def get_logger():

#     if not os.path.exists(LOG_DIR):
#         os.makedirs(LOG_DIR)

#     logger = logging.getLogger("FinBERT_ETL")

#     logger.setLevel(logging.INFO)

#     if logger.handlers:
#         return logger

#     formatter = logging.Formatter(

#         "%(asctime)s | %(levelname)s | %(message)s"

#     )

#     file_handler = logging.FileHandler(
#         LOG_FILE,
#         encoding="utf-8"
#     )

#     file_handler.setFormatter(formatter)

#     console_handler = logging.StreamHandler()

#     console_handler.setFormatter(formatter)

#     logger.addHandler(file_handler)

#     logger.addHandler(console_handler)

#     return logger

"""
==========================================================
Logger Module

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Creates and returns a reusable application logger.

Features
--------
✓ Console Logging
✓ File Logging
✓ Automatic Log Directory Creation
✓ Prevents Duplicate Handlers
==========================================================
"""

import logging
import os

from config import (
    LOG_DIR,
    LOG_FILE
)


def get_logger():
    """
    Creates and returns the application logger.
    """

    # Create log directory if it doesn't exist
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("FinBERT_ETL")

    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    # File Logger
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console Logger
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger