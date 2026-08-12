import streamlit as st


def metric_card(title, value, delta):

    st.markdown(
        f"""
<div class="metric-card">

<h4>{title}</h4>

<h2>{value}</h2>

<p>{delta}</p>

</div>
""",
        unsafe_allow_html=True,
    )