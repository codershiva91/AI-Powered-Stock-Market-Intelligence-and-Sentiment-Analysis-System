"""
==============================================================================
Technical Analyzer
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Performs technical analysis using the latest technical indicators.

Indicators Used
---------------
1. RSI (Relative Strength Index)
2. MACD
3. SMA 20
4. SMA 50
5. EMA 20
6. Bollinger Bands

Returns
-------
TechnicalResult

==============================================================================
"""

from ai.recommendation.constants import (
    RSI_OVERSOLD,
    RSI_OVERBOUGHT,
    TECHNICAL_SCORE,
)

from ai.recommendation.recommendation_models import TechnicalResult


class TechnicalAnalyzer:
    """
    Performs technical analysis using market indicators.
    """

    def analyze(
        self,
        technical_data: dict,
        stock_data: dict,
    ) -> TechnicalResult:

        result = TechnicalResult()

        if not technical_data:
            result.risks.append("Technical indicators are unavailable.")
            return result

        score = 0.0

        # ------------------------------------------------------------------
        # Read Technical Indicators
        # ------------------------------------------------------------------

        rsi = technical_data.get("rsi_14")

        macd = technical_data.get("macd")

        macd_signal = technical_data.get("macd_signal")

        sma20 = technical_data.get("sma_20")

        sma50 = technical_data.get("sma_50")

        ema20 = technical_data.get("ema_20")

        bb_upper = technical_data.get("bb_upper")

        bb_lower = technical_data.get("bb_lower")

        current_price = stock_data.get("close_price")

        # ------------------------------------------------------------------
        # RSI Analysis
        # ------------------------------------------------------------------

        if rsi is not None:

            if rsi < RSI_OVERSOLD:

                score += TECHNICAL_SCORE["RSI_BULLISH"]

                result.reasons.append(
                    f"RSI ({rsi:.2f}) indicates the stock is oversold."
                )

            elif rsi > RSI_OVERBOUGHT:

                score += TECHNICAL_SCORE["RSI_BEARISH"]

                result.risks.append(
                    f"RSI ({rsi:.2f}) indicates the stock is overbought."
                )

            else:

                result.reasons.append(
                    f"RSI ({rsi:.2f}) is within a healthy trading range."
                )

        # ------------------------------------------------------------------
        # MACD Analysis
        # ------------------------------------------------------------------

        if macd is not None and macd_signal is not None:

            if macd > macd_signal:

                score += TECHNICAL_SCORE["MACD_BULLISH"]

                result.reasons.append(
                    "MACD is above the signal line (Bullish crossover)."
                )

            else:

                score += TECHNICAL_SCORE["MACD_BEARISH"]

                result.risks.append(
                    "MACD is below the signal line (Bearish crossover)."
                )

        # ------------------------------------------------------------------
        # SMA Analysis
        # ------------------------------------------------------------------

        if sma20 is not None and sma50 is not None:

            if sma20 > sma50:

                score += TECHNICAL_SCORE["SMA_GOLDEN_CROSS"]

                result.reasons.append(
                    "SMA 20 is above SMA 50 (Bullish trend)."
                )

            else:

                score += TECHNICAL_SCORE["SMA_DEATH_CROSS"]

                result.risks.append(
                    "SMA 20 is below SMA 50 (Bearish trend)."
                )

        # ------------------------------------------------------------------
        # EMA Analysis
        # ------------------------------------------------------------------

        if current_price is not None and ema20 is not None:

            if current_price > ema20:

                score += TECHNICAL_SCORE["PRICE_ABOVE_EMA"]

                result.reasons.append(
                    "Current price is above EMA 20."
                )

            else:

                score += TECHNICAL_SCORE["PRICE_BELOW_EMA"]

                result.risks.append(
                    "Current price is below EMA 20."
                )

        # ------------------------------------------------------------------
        # Bollinger Band Analysis
        # ------------------------------------------------------------------

        if (
            current_price is not None
            and bb_upper is not None
            and bb_lower is not None
        ):

            if current_price > bb_upper:

                score += TECHNICAL_SCORE["BOLLINGER_BREAKOUT"]

                result.reasons.append(
                    "Price is trading above the upper Bollinger Band."
                )

            elif current_price < bb_lower:

                score += TECHNICAL_SCORE["BOLLINGER_BREAKDOWN"]

                result.risks.append(
                    "Price is trading below the lower Bollinger Band."
                )

        # ------------------------------------------------------------------
        # Final Score
        # ------------------------------------------------------------------

        result.score = score

        return result