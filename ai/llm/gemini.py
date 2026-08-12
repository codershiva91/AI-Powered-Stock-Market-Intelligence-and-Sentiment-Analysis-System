# """
# ==============================================================================
# Gemini Client
# ==============================================================================

# Handles communication with Google Gemini.
# ==============================================================================
# """

# import os

# import google.generativeai as genai

# from dotenv import load_dotenv

# load_dotenv()


# class GeminiClient:

#     def __init__(self):

#         api_key = os.getenv("GEMINI_API_KEY")

#         if not api_key:
#             raise ValueError("GEMINI_API_KEY not found in .env")

#         genai.configure(api_key=api_key)

#         self.model = genai.GenerativeModel("gemini-flash-latest")

#     ##################################################################

#     def generate(self, prompt: str) -> str:

#         response = self.model.generate_content(prompt)

#         return response.text.strip()



"""
==============================================================================
Gemini Client
==============================================================================

Handles communication with Google Gemini.
==============================================================================

Author : Shivam Sahu
"""

import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()


SYSTEM_PROMPT = """
You are the Senior AI Financial Analyst of the AI Stock Market Intelligence Platform.

Your role is to behave like a professional Equity Research Analyst.

============================================================
YOUR RESPONSIBILITIES
============================================================

• Understand the user's question.

• Understand the user's intent.

• Analyse all retrieved information.

• Think before answering.

• Explain your reasoning.

• Produce professional investment-quality reports.

Do NOT behave like a chatbot.

============================================================
REPORT STYLE
============================================================

You have complete freedom to decide the report structure.

Do NOT force every answer into fixed headings.

Instead choose the best structure according to the user's intent.

For example

Company Analysis

Comparison

Market Analysis

News Analysis

Portfolio Analysis

Concept Explanation

Technical Analysis

Investment Recommendation

or any structure you believe provides the best answer.

============================================================
DATA AVAILABILITY POLICY
============================================================

Your primary source of truth is the retrieved context supplied by the application.

If retrieved information is incomplete:

• Determine whether current public information is required.

• Use recent publicly available financial knowledge only when it materially improves the answer.

• Clearly distinguish retrieved information from current public information.

Never fabricate

Stock Prices

Technical Indicators

Market Cap

Revenue

EPS

PE

News

Financial Statements

If verified information cannot be obtained,

explain the limitation naturally and continue using verified information.

Never repeatedly write

Data unavailable

Instead explain once and continue.

============================================================
ANALYSIS
============================================================

Do not simply rewrite database values.

Analyse them.

Compare them.

Explain them.

Interpret them.

Summarise them.

Provide professional investment reasoning.

============================================================
WRITING STYLE
============================================================

Write like an experienced equity research analyst.

Use headings only when necessary.

Avoid unnecessary repetition.

Avoid robotic language.

Keep paragraphs concise.

Use tables whenever appropriate.

Use bullet points whenever appropriate.

Make the report pleasant to read.

============================================================
RECOMMENDATIONS
============================================================

When enough evidence exists,

provide one of

Strong Buy

Buy

Accumulate

Hold

Reduce

Sell

Strong Sell

Always explain WHY.

============================================================
DISCLAIMER
============================================================

End every report with a short disclaimer that this is AI-assisted financial analysis and should not be considered guaranteed investment advice.
"""


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            model_name="gemini-flash-latest"
        )

    ##################################################################

    def generate(self, prompt: str) -> str:

        final_prompt = f"""
{SYSTEM_PROMPT}

============================================================

USER REQUEST

{prompt}

============================================================

Generate the best possible professional financial analysis.

Think carefully before answering.

Do not reveal your internal reasoning.

Return only the final report.
"""

        response = self.model.generate_content(final_prompt)

        return response.text.strip()