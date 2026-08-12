"""
Professional Research Report Renderer

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform
"""

import streamlit as st

from ui.report.report_models import ResearchReport


class ReportRenderer:
    """
    Professional Dashboard Renderer
    """

    ###########################################################################
    # Main Renderer
    ###########################################################################

    def render(
        self,
        report: ResearchReport,
    ):

        if not report.success:

            st.error(report.error_message)

            return

        self.render_header(report)

        st.divider()

        self.render_dashboard(report)

    ###########################################################################
    # Header
    ###########################################################################

    def render_header(
        self,
        report: ResearchReport,
    ):

        with st.container(border=True):

            st.markdown(
                "# 📊 AI EQUITY RESEARCH REPORT"
            )

            st.markdown(
                f"## {report.company.upper()}"
            )

            st.caption(
                f"{report.report_type} • {report.investment_horizon}"
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Company",
                report.company,
            )

            c2.metric(
                "Report",
                report.report_type,
            )

            c3.metric(
                "Horizon",
                report.investment_horizon,
            )

            c4.metric(
                "Generated",
                report.generated_at.strftime("%d %b %Y"),
            )

    ###########################################################################
    # Dashboard
    ###########################################################################

    def render_dashboard(
        self,
        report: ResearchReport,
    ):

        if report.recommendation is None:

            return

        recommendation = report.recommendation.rating.upper()

        if recommendation == "BUY":

            badge = "🟢 BUY"

        elif recommendation == "SELL":

            badge = "🔴 SELL"

        else:

            badge = "🟡 HOLD"

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Recommendation",
                badge,
            )

        with c2:

            st.metric(
                "Confidence",
                f"{report.recommendation.confidence:.1f}%"
            )

        with c3:

            st.metric(
                "AI Score",
                f"{report.recommendation.score:.1f}/10"
            )

        with c4:

            risk = "Medium"

            if isinstance(
                report.risk_assessment,
                dict,
            ):

                risk = report.risk_assessment.get(
                    "overall_risk",
                    "Medium",
                )

            st.metric(
                "Risk",
                risk,
            )

        st.progress(
            report.recommendation.confidence / 100
        )

        if report.recommendation.summary:

            st.info(
                report.recommendation.summary
            )
            
    ###########################################################################
    # Generic Section Card
    ###########################################################################

    def _render_section(
        self,
        title: str,
        content,
    ):

        if not content:
            return

        with st.container(border=True):

            st.subheader(title)

            # ---------------------------------------------------------
            # String
            # ---------------------------------------------------------

            if isinstance(content, str):

                st.markdown(content)

            # ---------------------------------------------------------
            # Dictionary
            # ---------------------------------------------------------

            elif isinstance(content, dict):

                for key, value in content.items():

                    if value in ("", None, [], {}):

                        continue

                    st.markdown(
                        f"**{key.replace('_', ' ').title()}**"
                    )

                    st.write(value)

            # ---------------------------------------------------------
            # List
            # ---------------------------------------------------------

            elif isinstance(content, list):

                for item in content:

                    st.write(item)

            # ---------------------------------------------------------
            # Fallback
            # ---------------------------------------------------------

            else:

                st.write(content)

    ###########################################################################
    # Overview
    ###########################################################################

    def render_overview(
        self,
        report: ResearchReport,
    ):

        self._render_section(
            "📄 Executive Summary",
            report.executive_summary,
        )

        self._render_section(
            "📊 Market Snapshot",
            report.market_snapshot,
        )

        self._render_section(
            "🎯 Investment Thesis",
            report.investment_thesis,
        )

        self._render_section(
            "📝 Conclusion",
            report.conclusion,
        )

    ###########################################################################
    # Technical Analysis
    ###########################################################################

    def render_technical(
        self,
        report: ResearchReport,
    ):

        self._render_section(
            "📈 Technical Analysis",
            report.technical_analysis,
        )

    ###########################################################################
    # Fundamental Analysis
    ###########################################################################

    def render_fundamental(
        self,
        report: ResearchReport,
    ):

        self._render_section(
            "🏢 Fundamental Analysis",
            report.fundamental_analysis,
        )
        
    ###########################################################################
    # News Intelligence
    ###########################################################################

    def render_news(
        self,
        report: ResearchReport,
    ):

        self._render_section(
            "📰 News Intelligence",
            report.news_intelligence,
        )

    ###########################################################################
    # Sentiment Analysis
    ###########################################################################

    def render_sentiment(
        self,
        report: ResearchReport,
    ):

        self._render_section(
            "😊 Sentiment Analysis",
            report.sentiment_analysis,
        )

    ###########################################################################
    # Risk Assessment
    ###########################################################################

    def render_risk(
        self,
        report: ResearchReport,
    ):

        self._render_section(
            "⚠ Risk Assessment",
            report.risk_assessment,
        )

        self._render_section(
            "📊 Scenario Analysis",
            report.scenario_analysis,
        )

    ###########################################################################
    # Supporting Evidence
    ###########################################################################

    def render_evidence(
        self,
        report: ResearchReport,
    ):

        if not report.evidence:

            st.info("No supporting evidence available.")

            return

        for evidence in report.evidence:

            with st.container(border=True):

                st.subheader(evidence.title)

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Source",
                        evidence.source,
                    )

                with col2:

                    st.metric(
                        "Sentiment",
                        evidence.sentiment,
                    )

                with col3:

                    st.metric(
                        "Relevance",
                        f"{evidence.relevance_score:.2f}",
                    )

                if evidence.published_at:

                    st.caption(
                        f"Published : {evidence.published_at}"
                    )

                if evidence.snippet:

                    st.write(
                        evidence.snippet
                    )

    ###########################################################################
    # Data Sources
    ###########################################################################

    def render_sources(
        self,
        report: ResearchReport,
    ):

        if not report.data_sources:

            return

        st.subheader("🗂 Data Sources")

        cols = st.columns(4)

        for index, source in enumerate(report.data_sources):

            cols[index % 4].success(source) 
            

    ###########################################################################
    # Report Footer
    ###########################################################################

    def render_footer(
        self,
        report: ResearchReport,
    ):

        st.divider()

        col1, col2 = st.columns([3, 1])

        with col1:

            st.caption(
                f"""
Generated by **{report.generated_by}**

This report is AI-generated using structured market data,
technical indicators, company fundamentals, financial news,
and sentiment analysis.

It is intended for research and educational purposes only and
should not be considered financial advice.
"""
            )

        with col2:

            if report.generated_at:

                st.metric(
                    "Generated",
                    report.generated_at.strftime("%d %b %Y"),
                )

    ###########################################################################
    # Complete Dashboard
    ###########################################################################

    def render_complete_dashboard(
        self,
        report: ResearchReport,
    ):

        self.render_header(report)

        st.divider()

        self.render_dashboard(report)

        st.divider()

        tabs = st.tabs(
            [
                "📄 Overview",
                "📈 Technical",
                "🏢 Fundamental",
                "📰 News",
                "😊 Sentiment",
                "⚠ Risk",
                "📚 Evidence",
            ]
        )

        with tabs[0]:
            self.render_overview(report)

        with tabs[1]:
            self.render_technical(report)

        with tabs[2]:
            self.render_fundamental(report)

        with tabs[3]:
            self.render_news(report)

        with tabs[4]:
            self.render_sentiment(report)

        with tabs[5]:
            self.render_risk(report)

        with tabs[6]:
            self.render_evidence(report)

            st.divider()

            self.render_sources(report)

        self.render_footer(report)          
            
                               