import streamlit as st # to make web apps with Python

from welcome_screen import welcome_screen
from quiz_screen import quiz_screen
from end_screen import end_screen


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
    elif screen == "quiz":
        quiz_screen()
    elif screen == "end":
        end_screen()
    else:
        st.session_state.screen = "welcome"
        st.rerun()


if __name__ == "__main__":
    main()
