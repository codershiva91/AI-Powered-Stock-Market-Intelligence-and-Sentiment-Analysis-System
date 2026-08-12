"""
=========================================================
LLM Configuration
=========================================================

Author : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================================================
# Load .env explicitly from project root
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

print(f"Loading .env from: {ENV_PATH}")

load_dotenv(dotenv_path=ENV_PATH, override=True)

# ==========================================================
# Gemini Configuration
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "models/gemini-flash-latest"
).strip()

TEMPERATURE = 0.2
MAX_OUTPUT_TOKENS = 2048
TOP_P = 0.95
TOP_K = 40
TIMEOUT = 60

# ==========================================================
# Validation
# ==========================================================

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY was not loaded from .env")

print(f"API Key Prefix : {GEMINI_API_KEY[:8]}...")
print(f"Model          : {MODEL_NAME}")