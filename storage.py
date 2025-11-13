# storage.py
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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
