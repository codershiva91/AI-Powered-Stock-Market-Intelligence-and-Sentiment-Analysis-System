"""
==============================================================================
Fundamental Analyzer
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Evaluates company fundamentals to generate investment signals.

Metrics Used
------------
1. Trailing PE
2. Forward PE
3. Debt to Equity
4. Return on Equity (ROE)
5. Current Ratio
6. Quick Ratio
7. Operating Margin
8. Profit Margin
9. Dividend Yield
10. Price to Book

Returns
-------
FundamentalResult

==============================================================================
"""

from ai.recommendation.recommendation_models import FundamentalResult


class FundamentalAnalyzer:
    """
    Performs rule-based fundamental analysis.
    """

    def analyze(self, fundamental_data: dict) -> FundamentalResult:

        result = FundamentalResult()

        if not fundamental_data:

            result.risks.append(
                "Fundamental data is unavailable."
            )

            return result

        score = 0.0

        # ------------------------------------------------------------------
        # Read Fundamental Data
        # ------------------------------------------------------------------

        trailing_pe = fundamental_data.get("trailing_pe")
        forward_pe = fundamental_data.get("forward_pe")
        price_to_book = fundamental_data.get("price_to_book")

        debt_to_equity = fundamental_data.get("debt_to_equity")

        current_ratio = fundamental_data.get("current_ratio")
        quick_ratio = fundamental_data.get("quick_ratio")

        operating_margin = fundamental_data.get("operating_margin")
        profit_margin = fundamental_data.get("profit_margin")

        return_on_equity = fundamental_data.get("return_on_equity")

        dividend_yield = fundamental_data.get("dividend_yield")

        # ------------------------------------------------------------------
        # Trailing PE
        # ------------------------------------------------------------------

        if trailing_pe is not None:

            if trailing_pe < 25:

                score += 2

                result.reasons.append(
                    f"Trailing PE ({trailing_pe:.2f}) indicates reasonable valuation."
                )

            elif trailing_pe > 40:

                score -= 2

                result.risks.append(
                    f"Trailing PE ({trailing_pe:.2f}) indicates expensive valuation."
                )

        # ------------------------------------------------------------------
        # Forward PE
        # ------------------------------------------------------------------

        if (
            forward_pe is not None
            and trailing_pe is not None
        ):

            if forward_pe < trailing_pe:

                score += 2

                result.reasons.append(
                    "Forward PE is lower than Trailing PE, suggesting expected earnings growth."
                )

            else:

                score -= 1

                result.risks.append(
                    "Forward PE is higher than Trailing PE."
                )

        # ------------------------------------------------------------------
        # Debt to Equity
        # ------------------------------------------------------------------

        if debt_to_equity is not None:

            if debt_to_equity < 100:

                score += 2

                result.reasons.append(
                    f"Debt-to-Equity ({debt_to_equity:.2f}) is within a healthy range."
                )

            else:

                score -= 2

                result.risks.append(
                    f"High Debt-to-Equity ({debt_to_equity:.2f}) increases financial risk."
                )

        # ------------------------------------------------------------------
        # ROE
        # ------------------------------------------------------------------

        if return_on_equity is not None:

            if return_on_equity >= 0.15:

                score += 2

                result.reasons.append(
                    f"Strong Return on Equity ({return_on_equity:.2%})."
                )

            else:

                score -= 1

                result.risks.append(
                    f"Return on Equity ({return_on_equity:.2%}) is relatively low."
                )

        # ------------------------------------------------------------------
        # Current Ratio
        # ------------------------------------------------------------------

        if current_ratio is not None:

            if current_ratio >= 1:

                score += 1

                result.reasons.append(
                    f"Current Ratio ({current_ratio:.2f}) indicates good liquidity."
                )

            else:

                score -= 1

                result.risks.append(
                    f"Current Ratio ({current_ratio:.2f}) is below the ideal level."
                )

        # ------------------------------------------------------------------
        # Quick Ratio
        # ------------------------------------------------------------------

        if quick_ratio is not None:

            if quick_ratio >= 1:

                score += 1

                result.reasons.append(
                    f"Quick Ratio ({quick_ratio:.2f}) is healthy."
                )

            else:

                score -= 1

                result.risks.append(
                    f"Quick Ratio ({quick_ratio:.2f}) is below the recommended level."
                )

        # ------------------------------------------------------------------
        # Operating Margin
        # ------------------------------------------------------------------

        if operating_margin is not None:

            if operating_margin >= 0.15:

                score += 2

                result.reasons.append(
                    f"Healthy Operating Margin ({operating_margin:.2%})."
                )

            else:

                score -= 1

                result.risks.append(
                    f"Operating Margin ({operating_margin:.2%}) is relatively low."
                )

        # ------------------------------------------------------------------
        # Profit Margin
        # ------------------------------------------------------------------

        if profit_margin is not None:

            if profit_margin >= 0.10:

                score += 2

                result.reasons.append(
                    f"Strong Profit Margin ({profit_margin:.2%})."
                )

            else:

                score -= 1

                result.risks.append(
                    f"Profit Margin ({profit_margin:.2%}) is relatively low."
                )

        # ------------------------------------------------------------------
        # Price to Book
        # ------------------------------------------------------------------

        if price_to_book is not None:

            if price_to_book < 5:

                score += 1

                result.reasons.append(
                    f"Price-to-Book ({price_to_book:.2f}) appears reasonable."
                )

            else:

                score -= 1

                result.risks.append(
                    f"Price-to-Book ({price_to_book:.2f}) is relatively high."
                )

        # ------------------------------------------------------------------
        # Dividend Yield
        # ------------------------------------------------------------------

        if dividend_yield is not None:

            if dividend_yield > 0:

                score += 1

                result.reasons.append(
                    f"Dividend Yield ({dividend_yield:.2%}) provides shareholder returns."
                )

        # ------------------------------------------------------------------
        # Final Score
        # ------------------------------------------------------------------

        result.score = score

        return result