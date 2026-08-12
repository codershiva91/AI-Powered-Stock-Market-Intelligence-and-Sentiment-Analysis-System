
"""
AI Stock Market Intelligence Platform

Streamlit Entry Point
"""

from pathlib import Path
import sys

# =============================================================================
# Project Path Configuration
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# =============================================================================
# Streamlit
# =============================================================================

import streamlit as st

# =============================================================================
# UI Components
# =============================================================================

from styles.theme import apply_theme
from layout.header import render_header
from layout.footer import render_footer
from components.sidebar import render_sidebar


# =============================================================================
# Pages
# =============================================================================

from ui.pages.ai_assistant import render_ai_assistant
from ui.pages.about import render_about_page
from ui.pages.research_report import render_research_report



# =============================================================================
# Streamlit Configuration
# =============================================================================

st.set_page_config(
    page_title="AI Stock Market Intelligence Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# Main Application
# =============================================================================

def main():

    # --------------------------------------------------
    # Apply Global Theme
    # --------------------------------------------------

    apply_theme()

    # --------------------------------------------------
    # Sidebar
    # --------------------------------------------------

    page = render_sidebar()

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    render_header()

    # --------------------------------------------------
    # Page Routing
    # --------------------------------------------------

    if page == "📄 Research Report":
    
        render_research_report()
        
    elif page == "🤖 Financial AI Agent":

        render_ai_assistant()

    elif page == "📊 Company Analysis":

        st.title("📊 Company Analysis")
        st.info("🚧 Company Analysis page is under development.")

    elif page == "🌍 Market Analysis":

        st.title("🌍 Market Analysis")
        st.info("🚧 Market Analysis page is under development.")

    elif page == "📰 News Intelligence":

        st.title("📰 News Intelligence")
        st.info("🚧 News Intelligence page is under development.")

    elif page == "💼 Portfolio":

        st.title("💼 Portfolio")
        st.info("🚧 Portfolio page is under development.")

    elif page == "⚖️ Compare Companies":

        st.title("⚖️ Compare Companies")
        st.info("🚧 Compare Companies page is under development.")

    elif page == "ℹ️ About Us":

        render_about_page()

    elif page == "⚙️ Our Team":
        
        
        st.title("Our Team")
        
    else:

        st.title("Page Not Found")

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    render_footer()


# =============================================================================
# Application Entry
# =============================================================================

if __name__ == "__main__":
    main()