from google.oauth2 import service_account
from google.cloud import bigquery
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

CREDS = st.secrets["gcp_service_account"]

if not CREDS:
    raise ValueError("Missing Google Credentials!")

SCOPE = [
    'https://www.googleapis.com/auth/bigquery'
]

GOOGLE_CREDS = service_account.Credentials.from_service_account_info(
    CREDS,
    scopes=SCOPE
)

BQ_CLIENT = bigquery.Client(credentials=GOOGLE_CREDS, project=GOOGLE_CREDS.project_id)
PROJECT_ID = "mechanigo-liveagent"
DATASET_NAME = "conversations"