"""
=========================================================
Gemini Client
=========================================================

Author : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System
"""

import time

from google import genai
from google.genai import types
from google.genai.errors import ServerError

from ai.llm.config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    TOP_P,
    TOP_K,
    MAX_OUTPUT_TOKENS,
)

from ai.llm.logger import get_logger
from ai.llm.exceptions import GenerationError

logger = get_logger(__name__)


class GeminiClient:
    """
    Gemini LLM Client
    """

    def __init__(self):

        logger.info("Initializing Gemini Client...")

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        logger.info("Gemini Client initialized successfully.")

    def generate(self, prompt: str) -> str:
        """
        Generate response using Gemini.

        Parameters
        ----------
        prompt : str
            User prompt.

        Returns
        -------
        str
            Generated response.
        """

        retries = 3
        retry_delay = 5

        for attempt in range(1, retries + 1):

            try:

                logger.info(f"Sending request to Gemini (Attempt {attempt}/{retries})")
                logger.info(f"Using Model : {MODEL_NAME}")

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=TEMPERATURE,
                        top_p=TOP_P,
                        top_k=TOP_K,
                        max_output_tokens=MAX_OUTPUT_TOKENS,
                    ),
                )

                logger.info("Response received successfully.")

                if response.text:
                    return response.text

                return "No response generated."

            except ServerError as e:

                logger.warning(
                    f"Gemini server busy (503). Retry {attempt}/{retries}..."
                )

                if attempt < retries:
                    time.sleep(retry_delay)
                else:
                    raise GenerationError(
                        "Gemini service is temporarily unavailable. Please try again later."
                    ) from e

            except Exception as e:

                logger.exception("Gemini generation failed.")

                raise GenerationError(str(e)) from e