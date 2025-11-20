import streamlit as st # to make a Streamlit app
import gspread # Google Sheets access
from google.oauth2.service_account import Credentials # Google auth
from datetime import datetime # Date/time


SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]


@st.cache_resource
def get_worksheet():
    """
    Authenticate once, return the first worksheet.
    """
    creds_info = st.secrets["gcp_service_account"]
    creds = Credentials.from_service_account_info(creds_info, scopes=SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(st.secrets["SHEET_ID"])
    return sheet.sheet1


def save_result(name: str, score: int) -> None:
    """
    Append (name, score, timestamp) to the Google Sheet.
    """
    ws = get_worksheet()
    ws.append_row(
        [name, score, datetime.now().isoformat(timespec="seconds")],
        value_input_option="USER_ENTERED"
    )
