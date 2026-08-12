"""
About Page

AI Stock Market Intelligence Platform
"""

import streamlit as st


def render_about_page():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("ℹ️ About AI Stock Market Intelligence Platform")

    st.caption(
        "Enterprise AI-Powered Financial Intelligence Platform"
    )

    st.divider()

    # ==========================================================
    # Overview
    # ==========================================================

    st.subheader("🚀 Overview")

    st.write(
        """
The **AI Stock Market Intelligence Platform** is an enterprise-grade
financial intelligence system that combines Artificial Intelligence,
Machine Learning, Large Language Models, and Financial Analytics to
provide professional equity research and investment insights.

The platform integrates structured market data, technical indicators,
fundamental analysis, financial news, sentiment analysis, and AI reasoning
into a single intelligent financial assistant.
"""
    )

    # ==========================================================
    # Mission
    # ==========================================================

    st.divider()

    st.subheader("🎯 Mission")

    st.info(
        """
Empower investors with explainable AI, real-time market intelligence,
and professional research reports for informed investment decisions.
"""
    )

    # ==========================================================
    # Core Features
    # ==========================================================

    st.divider()

    st.subheader("✨ Core Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🤖 AI Financial Analyst")
        st.success("📈 Technical Analysis")
        st.success("💰 Fundamental Analysis")
        st.success("📰 News Intelligence")

    with col2:
        st.success("😊 Sentiment Analysis")
        st.success("📑 Equity Research Reports")
        st.success("📊 Company Comparison")
        st.success("🎯 AI Investment Recommendations")

    # ==========================================================
    # AI Architecture
    # ==========================================================

    st.divider()

    st.subheader("🧠 AI Architecture")

    st.code(
        """
User Query
      │
      ▼
Query Analyzer
      │
      ▼
LangGraph Workflow
      │
 ┌────┴──────────────┐
 ▼                   ▼
MariaDB         Qdrant Vector DB
 │                   │
 └─────────┬─────────┘
           ▼
      Gemini AI
           ▼
Professional Equity Research Report
""",
        language="text",
    )

    # ==========================================================
    # System Status
    # ==========================================================

    st.divider()

    st.subheader("🖥️ System Status")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ MariaDB")
        st.success("✅ Gemini")

    with col2:
        st.success("✅ Qdrant")
        st.success("✅ LangGraph")

    # ==========================================================
    # Platform Statistics
    # ==========================================================

    st.divider()

    st.subheader("📊 Platform Statistics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Companies", "50")

    with c2:
        st.metric("News Articles", "40,203")

    with c3:
        st.metric("AI Models", "4")

    # ==========================================================
    # Technology Stack
    # ==========================================================

    st.divider()

    st.subheader("⚙️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
### Frontend
- Streamlit

### Backend
- Python

### AI Framework
- LangGraph

### LLM
- Gemini
"""
        )

    with col2:

        st.markdown(
            """
### Database
- MariaDB

### Vector Database
- Qdrant

### NLP
- FinBERT

### Embeddings
- Sentence Transformers
"""
        )

    # ==========================================================
    # Developer
    # ==========================================================
from pathlib import Path

st.divider()

st.subheader("👨‍💻Developer")

col1, col2 = st.columns([1, 3])

with col1:

    image_path = Path(__file__).parent.parent / "assets" / "profile.png"

    st.image(
        str(image_path),
        width=180,
    )

with col2:

    st.markdown("## Shivam Sahu")
    
    st.markdown("**AI Engineer**")
    
    st.markdown("**AI & Data Science Enthusiast**")

    st.markdown(
        """
🎓 **Master of Computer Applications (MCA)**

💼 **Specialization**
- Artificial Intelligence
- Machine Learning
- Data Science
- Financial Analytics
- LLM Applications
- Generative AI

📍 India
"""
    )

    st.markdown(
        """
### 🔗 Connect with Me

- 💼 **LinkedIn:**https://www.linkedin.com/in/shivam-sahu91/

- 🐙 **GitHub:** https://github.com/codershiva91

- 📧 **Email:** Shivamsahu91.@gmail.com
"""
    )