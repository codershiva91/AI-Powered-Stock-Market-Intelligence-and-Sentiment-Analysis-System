"""
==============================================================================
Reusable Section Card
==============================================================================

Author : Shivam Sahu
==============================================================================

"""

import streamlit as st


def section_card(title: str, icon: str = "", border: bool = True):
    """
    Render a professional section header.

    Parameters
    ----------
    title : str
        Section title.

    icon : str
        Optional emoji/icon.

    border : bool
        Show divider.
    """

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            padding:16px 20px;
            border-radius:14px;
            border:1px solid #334155;
            margin-top:12px;
            margin-bottom:12px;
        ">
            <h4 style="
                color:white;
                margin:0;
                font-size:22px;
                font-weight:600;
            ">
                {icon} {title}
            </h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if border:
        st.divider()