import streamlit as st

def is_valid_name(name: str) -> bool:
    """
    Return True if the name is at least 3 characters (after stripping)
    and contains no digits; otherwise return False.
    """
    cleaned = name.strip()
    return len(cleaned) >= 3 and not any(ch.isdigit() for ch in cleaned)

def welcome_screen():
    st.title("Times Tables Quiz")

    name = st.text_input("Your name", value=st.session_state.get("name", ""))
    st.session_state.name = name

    if st.button("Start quiz"):
        if not is_valid_name(name):
            st.error("Name must be at least 3 characters long and must not contain digits.")
        else:
            st.write(f"Hello, {name}")
            st.session_state.screen = "quiz"
            st.rerun()