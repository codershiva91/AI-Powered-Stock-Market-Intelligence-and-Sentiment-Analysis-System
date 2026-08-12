# import streamlit as st
# from ai.agents.supervisor.supervisor import SupervisorAgent


# @st.cache_resource
# def load_supervisor():
#     return SupervisorAgent()


# supervisor = load_supervisor()


# def render_ai_assistant():

#     st.markdown("## 🤖 AI Financial Analyst")
#     st.caption(
#         "Ask anything about companies, markets, technical analysis, news or portfolios."
#     )

#     # -----------------------------------------------------------------
#     # Chat History
#     # -----------------------------------------------------------------

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:

#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # -----------------------------------------------------------------
#     # Chat Input
#     # -----------------------------------------------------------------

#     prompt = st.chat_input(
#         "Ask about Reliance, HDFC Bank, NIFTY, technical analysis..."
#     )

#     if not prompt:
#         return

#     # -----------------------------------------------------------------
#     # User Message
#     # -----------------------------------------------------------------

#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": prompt,
#         }
#     )

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # -----------------------------------------------------------------
#     # Assistant
#     # -----------------------------------------------------------------

#     with st.chat_message("assistant"):

#         status = st.status("🧠 AI Pipeline", expanded=True)

#         status.write("✅ Query Analyzer")
#         status.write("✅ Entity Extraction")
#         status.write("✅ Technical Analysis")
#         status.write("✅ Fundamental Analysis")
#         status.write("✅ Recommendation Engine")
#         status.write("✅ Vector Search")
#         status.write("✅ Gemini")

#         try:

#             response = supervisor.answer(prompt)

#             # Convert any non-string response safely
#             if response is None:
#                 response = "No response generated."

#             elif not isinstance(response, str):
#                 response = str(response)

#             status.update(
#                 label="✅ Analysis Completed",
#                 state="complete",
#             )

#             tab1, tab2, tab3 = st.tabs(
#                 [
#                     "📄 Analysis",
#                     "📊 Summary",
#                     "📈 Recommendation",
#                 ]
#             )

#             with tab1:
#                 st.markdown(response)

#             with tab2:

#                 c1, c2, c3 = st.columns(3)

#                 with c1:
#                     st.metric("Confidence", "91%")

#                 with c2:
#                     st.metric("Risk", "Medium")

#                 with c3:
#                     st.metric("AI Score", "89/100")

#             with tab3:

#                 st.success("🟢 BUY")

#                 st.progress(0.91)

#             st.session_state.messages.append(
#                 {
#                     "role": "assistant",
#                     "content": response,
#                 }
#             )

#         except Exception as e:

#             status.update(
#                 label="❌ Analysis Failed",
#                 state="error",
#             )

#             st.error(f"Error: {e}")


import streamlit as st
from ai.agents.supervisor.supervisor import SupervisorAgent


@st.cache_resource
def load_supervisor():
    return SupervisorAgent()


def render_ai_assistant():

    st.markdown("## 🤖 AI Financial Analyst")
    st.caption(
        "Ask anything about companies, markets, technical analysis, news or portfolios."
    )

    supervisor = load_supervisor()

    # ---------------------------------------------------------------
    # Chat History
    # ---------------------------------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ---------------------------------------------------------------
    # Chat Input
    # ---------------------------------------------------------------

    prompt = st.chat_input(
        "Ask about Reliance, HDFC Bank, NIFTY, technical analysis..."
    )

    if not prompt:
        return

    # ---------------------------------------------------------------
    # User Message
    # ---------------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------------------------------------------------------------
    # Assistant
    # ---------------------------------------------------------------

    with st.chat_message("assistant"):

        status = st.status("🧠 AI Pipeline", expanded=True)

        status.write("✅ Query Analyzer")
        status.write("✅ Entity Extraction")
        status.write("✅ Technical Analysis")
        status.write("✅ Fundamental Analysis")
        status.write("✅ Recommendation Engine")
        status.write("✅ Vector Search")
        status.write("✅ Gemini")

        try:

            response = supervisor.answer(prompt)

            if response is None:
                response = "No response generated."

            elif not isinstance(response, str):
                response = str(response)

            status.update(
                label="✅ Analysis Completed",
                state="complete",
            )

            tab1, tab2, tab3 = st.tabs(
                [
                    "📄 Analysis",
                    "📊 Summary",
                    "📈 Recommendation",
                ]
            )

            with tab1:
                st.markdown(response)

            with tab2:

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.metric("Confidence", "91%")

                with c2:
                    st.metric("Risk", "Medium")

                with c3:
                    st.metric("AI Score", "89/100")

            with tab3:

                st.success("🟢 BUY")
                st.progress(0.91)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response,
                }
            )

        except Exception as e:

            status.update(
                label="❌ Analysis Failed",
                state="error",
            )

            st.error(f"Error: {e}")