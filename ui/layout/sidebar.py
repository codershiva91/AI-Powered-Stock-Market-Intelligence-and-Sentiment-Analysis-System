import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("📈 AI Intelligence")

        st.divider()

        st.page_link("pages/dashboard.py", label="🏠 Dashboard")

        st.page_link("pages/ai_assistant.py", label="🤖 AI Analyst")

        st.page_link("pages/company_analysis.py", label="📊 Company")

        st.page_link("pages/news.py", label="📰 News")

        st.page_link("pages/portfolio.py", label="💼 Portfolio")

        st.divider()

        st.subheader("System Status")

        st.success("MariaDB")

        st.success("Qdrant")

        st.success("Gemini")

        st.success("LangGraph")

        st.caption("Version 2.0")