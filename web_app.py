import streamlit as st
from streamlit_chat import message
import uuid


def build_web_app(ask):
    def answer_request():
        if st.session_state.text_input:
            with st.spinner("Generating response..."):
                generated_response = ask(st.session_state.text_input)
                st.session_state.chat_history.insert(
                    0, (st.session_state.text_input, generated_response["output"])
                )
                st.session_state.user_prompt_history.insert(
                    0, st.session_state.text_input
                )
                st.session_state.chat_answers_history.insert(
                    0, generated_response["output"]
                )
            st.session_state.text_input = ""

    st.header("Jira Bot")
    if (
        "chat_answers_history" not in st.session_state
        and "user_prompt_history" not in st.session_state
        and "chat_history" not in st.session_state
        and "text_input" not in st.session_state
    ):
        st.session_state["chat_answers_history"] = []
        st.session_state["user_prompt_history"] = []
        st.session_state["chat_history"] = []
        st.session_state.text_input = ""

    prompt = st.text_area("Prompt", key="text_input", on_change=answer_request)
    if st.session_state["chat_answers_history"]:

        for generated_response, user_query in zip(
            st.session_state["chat_answers_history"],
            st.session_state["user_prompt_history"],
        ):
            message(user_query, is_user=True, key=str(uuid.uuid4()))
            message(generated_response, is_user=False, key=str(uuid.uuid4()))
