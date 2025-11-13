import streamlit as st # for web interfaces with Python
from welcome_screen import welcome_screen
from question_generator import generate_question

TOTAL_QUESTIONS = 10

def init_state() -> None:
    """Set default values in session_state if they are missing."""
    st.session_state.setdefault("screen", "welcome")
    st.session_state.setdefault("name", "")
    st.session_state.setdefault("question_number", 1)
    st.session_state.setdefault("score", 0)
    st.session_state.setdefault("question", None)
    st.session_state.setdefault("saved", False)
    st.session_state.setdefault("total_questions", TOTAL_QUESTIONS)


def main() -> None:
    init_state()

    screen = st.session_state.screen

    if screen == "welcome":
        welcome_screen()
    else:
        # Fallback – go back to welcome if something weird happens
        st.session_state.screen = "welcome"
        st.rerun()


if __name__ == "__main__":
    main()