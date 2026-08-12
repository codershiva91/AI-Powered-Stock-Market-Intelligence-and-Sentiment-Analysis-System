import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ----------------------------
Main App
-----------------------------*/

.stApp{

    background:#0F172A;

    color:white;

}

/* ----------------------------
Sidebar
-----------------------------*/

section[data-testid="stSidebar"]{

    background:#111827;

    border-right:1px solid #334155;

}

/* ----------------------------
Metric Card
-----------------------------*/

.metric-card{

    background:#1E293B;

    border-radius:18px;

    padding:22px;

    border:1px solid #334155;

    transition:0.25s;

}

.metric-card:hover{

    border:1px solid #2563EB;

    transform:translateY(-4px);

}

/* ----------------------------
Section Card
-----------------------------*/

.section-card{

    background:#1E293B;

    border-radius:18px;

    padding:24px;

    margin-bottom:20px;

    border:1px solid #334155;

}

/* ----------------------------
Title
-----------------------------*/

.page-title{

    color:white;

    font-size:38px;

    font-weight:700;

}

.page-subtitle{

    color:#94A3B8;

    font-size:18px;

}

/* ----------------------------
Buttons
-----------------------------*/

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:12px;

    height:50px;

    width:100%;

    font-size:16px;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* ----------------------------
Text Input
-----------------------------*/

.stTextInput input{

    border-radius:12px;

}

</style>
""",
        unsafe_allow_html=True,
    )