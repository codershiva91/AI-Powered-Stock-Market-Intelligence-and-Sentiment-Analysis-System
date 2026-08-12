"""
==============================================================================
Dashboard
==============================================================================

AI Stock Market Intelligence Platform

Author : Shivam Sahu
==============================================================================
"""

import streamlit as st

from widgets.metric_card import metric_card


def render_dashboard():

    st.title("🏠 Dashboard")

    st.caption(
        "Real-Time Indian Stock Market Overview"
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(
            "NIFTY 50",
            "25,742",
            "+0.82%"
        )

    with c2:

        metric_card(
            "SENSEX",
            "84,315",
            "+0.74%"
        )

    with c3:

        metric_card(
            "USD / INR",
            "86.13",
            "-0.14%"
        )

    with c4:

        metric_card(
            "Market Mood",
            "Bullish",
            "AI Score 91%"
        )

    st.write("")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("📈 Top Gainers")

        st.dataframe(
            {
                "Company": [
                    "Reliance",
                    "Infosys",
                    "Adani Ports",
                    "TCS",
                    "L&T"
                ],
                "Gain %": [
                    2.41,
                    2.12,
                    1.88,
                    1.54,
                    1.33
                ]
            },
            use_container_width=True
        )

        st.subheader("📉 Top Losers")

        st.dataframe(
            {
                "Company": [
                    "HDFC Bank",
                    "Asian Paints",
                    "Kotak",
                    "Titan",
                    "ITC"
                ],
                "Loss %": [
                    -1.82,
                    -1.55,
                    -1.21,
                    -0.94,
                    -0.61
                ]
            },
            use_container_width=True
        )

    with right:

        st.subheader("📰 Latest News")

        st.info(
            "RBI keeps repo rate unchanged."
        )

        st.info(
            "Reliance announces new AI initiative."
        )

        st.info(
            "Infosys signs multi-billion dollar contract."
        )

        st.write("")

        st.subheader("⭐ Watchlist")

        st.success("Reliance")

        st.success("TCS")

        st.success("Infosys")

        st.success("ICICI Bank")