"""
==============================================================================
Report Prompt Builder

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform
==============================================================================
"""


class ReportPromptBuilder:
    """
    Builds the prompt used to generate
    a professional research report.
    """

    ##########################################################################

    def build(
        self,
        config: dict,
    ) -> str:
        """
        Build prompt for generating a structured institutional
        equity research report.
        """

        return f"""
You are a Senior Equity Research Analyst working for an institutional investment firm.

Your task is to generate a professional equity research report.

Return ONLY valid JSON.

DO NOT:

- Use Markdown
- Use ```json
- Explain anything
- Add comments
- Add extra keys
- Skip any keys

Every key MUST exist.

If information is unavailable, use:

- "" for strings
- 0 for numbers
- [] for arrays
- {{}} for objects

Never invent financial data.

Only use information provided by the AI context.

Company:
{config["company"]}

Report Type:
{config["report_type"]}

Investment Horizon:
{config["investment_horizon"]}

Include Sections:
{list(config["include_sections"].keys())}

{{
    "company": "",
    "report_type": "",
    "investment_horizon": "",
    "generated_at": "",

    "recommendation":
    {{
        "rating": "",
        "confidence": 0,
        "score": 0,
        "summary": "",
        "risk_level": "",
        "target_price": "",
        "expected_return": ""
    }},

    "executive_summary": "",

    "market_snapshot":
    {{
        "current_price": "",
        "market_cap": "",
        "sector": "",
        "industry": "",
        "volume": "",
        "52_week_high": "",
        "52_week_low": ""
    }},

    "technical_analysis":
    {{
        "trend": "",
        "rsi": "",
        "macd": "",
        "sma20": "",
        "sma50": "",
        "bollinger_band": "",
        "support": "",
        "resistance": "",
        "analysis": ""
    }},

    "fundamental_analysis":
    {{
        "pe_ratio": "",
        "forward_pe": "",
        "pb_ratio": "",
        "roe": "",
        "profit_margin": "",
        "operating_margin": "",
        "analysis": ""
    }},

    "news_intelligence": "",

    "sentiment_analysis":
    {{
        "overall_sentiment": "",
        "confidence": "",
        "summary": ""
    }},

    "risk_assessment":
    {{
        "overall_risk": "",
        "business_risk": "",
        "financial_risk": "",
        "market_risk": "",
        "summary": ""
    }},

    "scenario_analysis":
    {{
        "bull_case": "",
        "base_case": "",
        "bear_case": ""
    }},

    "investment_thesis": "",

    "evidence":
    [
        {{
            "title": "",
            "source": "",
            "description": "",
            "sentiment": ""
        }}
    ],

    "data_sources":
    [
        ""
    ]
}}
"""