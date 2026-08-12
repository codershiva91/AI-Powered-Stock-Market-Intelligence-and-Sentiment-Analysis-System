"""
=========================================================
Query Processor
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Pre-processes user queries before semantic retrieval.

Responsibilities
----------------
1. Normalize whitespace
2. Remove unnecessary punctuation
3. Expand finance abbreviations
4. Normalize company names
5. Return cleaned query

=========================================================
"""

import re


class QueryProcessor:
    """
    Processes user search queries.
    """

    # =====================================================

    COMPANY_ALIASES = {

        "ril": "Reliance Industries",
        "reliance": "Reliance Industries",

        "tcs": "Tata Consultancy Services",

        "hdfc": "HDFC Bank",

        "sbi": "State Bank of India",

        "icici": "ICICI Bank",

        "hul": "Hindustan Unilever",

        "itc": "ITC",

        "ntpc": "NTPC",

        "ongc": "ONGC",

        "adani": "Adani Group",

        "infosys": "Infosys",

        "wipro": "Wipro",

        "zomato": "Zomato",

        "paytm": "Paytm"
    }

    # =====================================================

    FINANCIAL_TERMS = {

        "q1": "quarter 1",
        "q2": "quarter 2",
        "q3": "quarter 3",
        "q4": "quarter 4",

        "eps": "earnings per share",

        "pe": "price earnings ratio",

        "roi": "return on investment",

        "ipo": "initial public offering",

        "fii": "foreign institutional investors",

        "dii": "domestic institutional investors"
    }

    # =====================================================

    @staticmethod
    def clean(query: str) -> str:
        """
        Basic query cleaning.
        """

        query = query.strip()

        query = re.sub(r"\s+", " ", query)

        return query

    # =====================================================

    @classmethod
    def expand_financial_terms(cls, query: str) -> str:
        """
        Expand finance abbreviations.
        """

        words = query.split()

        expanded = []

        for word in words:

            key = word.lower()

            expanded.append(
                cls.FINANCIAL_TERMS.get(key, word)
            )

        return " ".join(expanded)

    # =====================================================

    @classmethod
    def normalize_company_names(cls, query: str) -> str:
        """
        Normalize company aliases.
        """

        words = query.split()

        normalized = []

        for word in words:

            key = word.lower()

            normalized.append(
                cls.COMPANY_ALIASES.get(key, word)
            )

        return " ".join(normalized)

    # =====================================================

    @classmethod
    def process(cls, query: str) -> str:
        """
        Complete query processing pipeline.
        """

        query = cls.clean(query)

        query = cls.expand_financial_terms(query)

        query = cls.normalize_company_names(query)

        return query