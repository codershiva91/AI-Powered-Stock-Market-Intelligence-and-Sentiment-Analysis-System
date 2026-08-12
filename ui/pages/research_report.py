
"""
Professional Research Report Page

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence Platform
"""

import streamlit as st

from ui.report.report_generator import ResearchReportGenerator
from ui.report.pdf_exporter import PDFExporter
from ui.report.report_renderer import ReportRenderer


# =============================================================================
# Research Report Page
# =============================================================================

def render_research_report():
      

    # -------------------------------------------------------------------------
    # Page Header
    # -------------------------------------------------------------------------

    st.title("📊 AI Equity Research Dashboard")

    st.caption(
        "Generate institutional-grade AI research reports powered by your Stock Market Intelligence Platform."
    )

    st.divider()

    # -------------------------------------------------------------------------
    # Layout
    # -------------------------------------------------------------------------

    left_panel, right_panel = st.columns(
        [1, 2.2],
        gap="large",
    )


# =========================================================================
# LEFT PANEL
# =========================================================================

    with left_panel:

        st.subheader("AI Driven Financial Report")

        company = st.text_input(
        "Company",
        placeholder="Example: Infosys",
        key="research_company_input",
    )

    report_type = st.selectbox(
        "Report Type",
        [
            "Company Analysis",
            "Technical Analysis",
            "Fundamental Analysis",
            "Investment Recommendation",
            "News Intelligence",
            "Company Comparison",
        ],
    )

    investment_horizon = st.selectbox(
        "Investment Horizon",
        [
            "Short Term",
            "Medium Term",
            "Long Term",
        ],
    )

    st.divider()

    # ==========================================================
    # Report Sections
    # ==========================================================

    st.subheader("📑 Report Sections")

    selected_sections = st.multiselect(
        "Select Report Sections",
        options=[
            "Executive Summary",
            "AI Recommendation Dashboard",
            "Market Snapshot",
            "Technical Analysis",
            "Fundamental Analysis",
            "News Intelligence",
            "Sentiment Analysis",
            "Risk Assessment",
            "Scenario Analysis",
            "Investment Thesis",
            "Supporting Evidence",
            "Data Sources",
        ],
        default=[
            "Executive Summary",
            "AI Recommendation Dashboard",
            "Market Snapshot",
            "Technical Analysis",
            "Fundamental Analysis",
            "News Intelligence",
            "Sentiment Analysis",
            "Risk Assessment",
            "Scenario Analysis",
            "Investment Thesis",
            "Supporting Evidence",
            "Data Sources",
        ],
    )

    executive = "Executive Summary" in selected_sections
    recommendation = "AI Recommendation Dashboard" in selected_sections
    market = "Market Snapshot" in selected_sections
    technical = "Technical Analysis" in selected_sections
    fundamental = "Fundamental Analysis" in selected_sections
    news = "News Intelligence" in selected_sections
    sentiment = "Sentiment Analysis" in selected_sections
    risk = "Risk Assessment" in selected_sections
    scenario = "Scenario Analysis" in selected_sections
    thesis = "Investment Thesis" in selected_sections
    evidence = "Supporting Evidence" in selected_sections
    sources = "Data Sources" in selected_sections

    st.divider()

    # ==========================================================
    # Output
    # ==========================================================

    st.subheader("📄 Output")

    output = st.radio(
        "Output Format",
        [
            "Dashboard",
            "PDF",
            "Dashboard + PDF",
        ],
    )

    include_charts = st.checkbox(
        "Include Charts",
        value=True,
    )

    include_tables = st.checkbox(
        "Include Tables",
        value=True,
    )

    include_logo = st.checkbox(
        "Include Company Logo",
        value=True,
    )

    st.divider()

    # ==========================================================
    # Generate Button
    # ==========================================================

    if st.button(
        "🚀 Generate Professional Report",
        use_container_width=True,
        type="primary",
    ):

        if not company.strip():

            st.warning("Please enter a company name.")
            st.stop()

        config = {
            "company": company,
            "report_type": report_type,
            "investment_horizon": investment_horizon,
            "output": output,
            "include_sections": {
                "executive": executive,
                "market": market,
                "technical": technical,
                "fundamental": fundamental,
                "news": news,
                "sentiment": sentiment,
                "risk": risk,
                "scenario": scenario,
                "thesis": thesis,
                "evidence": evidence,
                "sources": sources,
            },
            "include_charts": include_charts,
            "include_tables": include_tables,
            "include_logo": include_logo,
        }

        with st.spinner(
            "🤖 AI Agents are analyzing structured and unstructured market intelligence..."
        ):

            try:

                generator = ResearchReportGenerator()

                report = generator.generate(config)

                if report.success:

                    st.session_state["generated_report"] = report

                    st.success(
                        "✅ Professional Research Report Generated Successfully"
                    )

                else:

                    st.error(report.error_message)

            except Exception as e:

                st.exception(e)


# =========================================================================
# RIGHT PANEL
# =========================================================================

    with right_panel:

        report = st.session_state.get("generated_report")

    # ------------------------------------------------------------
    # Empty State
    # ------------------------------------------------------------

    if report is None:

        st.info(
            """
## 📊 AI Research Dashboard

Generate an institutional-grade research report.

The dashboard includes:

- Executive Summary
- Market Snapshot
- Technical Analysis
- Fundamental Analysis
- News Intelligence
- Sentiment Analysis
- Risk Assessment
- Supporting Evidence
- Professional PDF Export
"""
        )

    # ------------------------------------------------------------
    # Error State
    # ------------------------------------------------------------

    elif not report.success:

        st.error(report.error_message)

    # ------------------------------------------------------------
    # Report Dashboard
    # ------------------------------------------------------------

    else:

        renderer = ReportRenderer()

        (
            overview_tab,
            technical_tab,
            fundamental_tab,
            news_tab,
            sentiment_tab,
            risk_tab,
            evidence_tab,
        ) = st.tabs(
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

        # ==========================================================
        # OVERVIEW
        # ==========================================================

        with overview_tab:

            renderer.render_header(report)

            st.divider()

            renderer.render_dashboard(report)

            st.divider()

            renderer.render_overview(report)

        # ==========================================================
        # TECHNICAL
        # ==========================================================

        with technical_tab:

            renderer.render_technical(report)

        # ==========================================================
        # FUNDAMENTAL
        # ==========================================================

        with fundamental_tab:

            renderer.render_fundamental(report)

        # ==========================================================
        # NEWS
        # ==========================================================

        with news_tab:

            renderer.render_news(report)

        # ==========================================================
        # SENTIMENT
        # ==========================================================

        with sentiment_tab:

            renderer.render_sentiment(report)

        # ==========================================================
        # RISK
        # ==========================================================

        with risk_tab:

            renderer.render_risk(report)

        # ==========================================================
        # EVIDENCE
        # ==========================================================

        with evidence_tab:

            renderer.render_evidence(report)

        # ==========================================================
        # PDF EXPORT
        # ==========================================================

        st.divider()

        st.subheader("📄 Export Research Report")

        st.caption(
            "Download a professionally formatted institutional research report."
        )

        try:

            exporter = PDFExporter()

            pdf_buffer = exporter.export(report)

            if pdf_buffer:

                st.download_button(
                    label="📄 Download Professional Research Report",
                    data=pdf_buffer,
                    file_name=f"{report.company}_Research_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            else:

                st.error("Unable to generate PDF report.")

        except Exception as e:

            st.error("PDF Export Failed")
            st.exception(e)

        st.markdown("---")

        st.caption(
            "© AI Stock Market Intelligence Platform | Professional Equity Research Dashboard"
        )
        
#render_research_report()