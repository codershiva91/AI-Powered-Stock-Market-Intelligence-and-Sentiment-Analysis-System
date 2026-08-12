"""
=========================================================
Evaluation Configuration
=========================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Central configuration for the Evaluation module.

Responsibilities
----------------
1. Benchmark dataset configuration
2. Evaluation settings
3. Performance thresholds
4. Result output configuration

=========================================================
"""

from pathlib import Path

# =====================================================
# Base Directory
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

# =====================================================
# Benchmark Configuration
# =====================================================

BENCHMARK_FILE = BASE_DIR / "benchmark_questions.json"

# =====================================================
# Output Configuration
# =====================================================

OUTPUT_DIR = BASE_DIR / "results"

OUTPUT_FILE = OUTPUT_DIR / "evaluation_report.csv"

# =====================================================
# Evaluation Settings
# =====================================================

DEFAULT_TOP_K = 10

TOTAL_TESTS = 50

# =====================================================
# Performance Thresholds
# =====================================================

MIN_RETRIEVAL_SCORE = 0.65

MAX_RESPONSE_TIME = 5.0  # seconds

# =====================================================
# Logging
# =====================================================

LOG_LEVEL = "INFO"

# =====================================================
# Report Settings
# =====================================================

SAVE_RESULTS = True

PRINT_SUMMARY = True