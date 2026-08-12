import streamlit as st


def render_header():

    left, right = st.columns([5, 1])

    with left:

        st.markdown(
            """
<div class="page-title">

📈 AI Stock Market Intelligence Platform

</div>

<div class="page-subtitle">

Enterprise AI Powered Financial Intelligence Platform

</div>
""",
            unsafe_allow_html=True,
        )

    with right:

        st.metric(
            "AI Status",
            "🟢 Online",
        )

    st.divider()