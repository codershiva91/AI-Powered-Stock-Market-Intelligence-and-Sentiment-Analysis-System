"""
==============================================================================
Alias Generator
==============================================================================

Project : AI-Driven Stock Market Intelligence System

Description
-----------
Generates searchable aliases for companies using symbol_master and
manual aliases.

Responsibilities
----------------
1. Remove .NS suffix
2. Normalize company names
3. Generate automatic aliases
4. Merge manual aliases
5. Compile regex patterns

==============================================================================
"""

import re
from typing import Dict, List

from news_mapping.company_aliases import COMPANY_ALIASES
from ai.common.logger import get_logger

logger = get_logger(__name__)


class AliasGenerator:

    """
    Generates aliases and compiled regex patterns
    for company matching.
    """

    def __init__(self, companies: List[Dict]):

        self.companies = companies

    # ------------------------------------------------------------------

    @staticmethod
    def normalize(text: str) -> str:

        """
        Normalize text.
        """

        if not text:
            return ""

        text = text.lower()

        text = re.sub(r"[^a-z0-9& ]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # ------------------------------------------------------------------

    @staticmethod
    def clean_symbol(symbol: str) -> str:

        """
        Remove .NS suffix.
        """

        return symbol.replace(".NS", "").strip()

    # ------------------------------------------------------------------

    @staticmethod
    def generate_name_aliases(company_name: str) -> List[str]:

        """
        Automatically generate aliases.
        """

        aliases = set()

        aliases.add(company_name)

        words = company_name.split()

        if len(words) >= 2:
            aliases.add(words[0])

        stop_words = {
            "limited",
            "ltd",
            "industries",
            "corporation",
            "company",
            "bank",
            "services"
        }

        cleaned = [
            word
            for word in words
            if word.lower() not in stop_words
        ]

        if cleaned:
            aliases.add(" ".join(cleaned))

        return list(aliases)

    # ------------------------------------------------------------------

    @staticmethod
    def compile_patterns(aliases: List[str]):

        """
        Compile regex patterns.
        """

        patterns = []

        for alias in aliases:

            alias = alias.strip()

            if not alias:
                continue

            pattern = re.compile(
                rf"\b{re.escape(alias.lower())}\b",
                re.IGNORECASE
            )

            patterns.append(pattern)

        return patterns

    # ------------------------------------------------------------------

    def build(self):

        """
        Build alias objects.
        """

        company_objects = []

        for company in self.companies:

            symbol = self.clean_symbol(
                company["symbol"]
            )

            company_name = company["company_name"]

            aliases = set()

            aliases.update(

                self.generate_name_aliases(

                    company_name

                )

            )

            aliases.add(symbol)

            manual = COMPANY_ALIASES.get(symbol, [])

            aliases.update(manual)

            compiled = self.compile_patterns(

                list(aliases)

            )

            company_objects.append({

                "symbol": symbol,

                "patterns": compiled

            })

        logger.info(

            "Generated aliases for %d companies.",

            len(company_objects)

        )

        return company_objects