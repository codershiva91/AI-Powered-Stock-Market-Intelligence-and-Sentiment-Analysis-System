"""
Sidebar Component

AI Stock Market Intelligence Platform
"""

import streamlit as st


def render_sidebar() -> str:
    """
    Render the application sidebar.

    Returns:
        str: Selected page name.
    """

    with st.sidebar:

        # ==========================================================
        # Logo
        # ==========================================================

        st.markdown("# 📈 AI Intelligence")

        st.markdown(
            """
            <p style='color:#94A3B8; margin-top:-10px;'>
            Enterprise Financial Intelligence Platform
            </p>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # ==========================================================
        # Navigation
        # ==========================================================

        pages = [
            "📄 Research Report",
            "🤖 Financial AI Agent",
            "📊 Company Analysis",
            "🌍 Market Analysis",
            "📰 News Intelligence",
            "💼 Portfolio",
            "⚖️ Compare Companies",
            "ℹ️ About Us",
            "⚙️ Our Team",
        ]

        if "selected_page" not in st.session_state:
            st.session_state.selected_page = "🤖 Financial AI Agent"
        for p in pages:

            selected = st.session_state.selected_page == p

            if st.button(
                p,
                key=f"nav_{p}",
                use_container_width=True,
                type="primary" if selected else "secondary",
            ):
                st.session_state.selected_page = p
                st.rerun()

        page = st.session_state.selected_page

        st.divider()

        # ==========================================================
        # Platform
        # ==========================================================

        st.metric("AI Models", "4")

        st.divider()

        st.caption("🚀 AI Stock Market Intelligence Platform")
        st.caption("Version 2.0.0")

    return page