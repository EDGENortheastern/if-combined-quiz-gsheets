import streamlit as st # web apps with Python
from storage import save_result


def end_screen() -> None:
    name = st.session_state.name
    score = st.session_state.score
    total = st.session_state.get("total_questions", 10)

    st.title("Quiz complete!")
    st.subheader(f"{name}, your score is {score} / {total}")

    if not st.session_state.saved:
        save_result(name, score)
        st.session_state.saved = True
        st.success("Your result has been saved.")

    if st.button("Play again"):
        st.session_state.question_number = 1
        st.session_state.score = 0
        st.session_state.question = None
        st.session_state.saved = False
        st.session_state.screen = "welcome"
        st.rerun()
