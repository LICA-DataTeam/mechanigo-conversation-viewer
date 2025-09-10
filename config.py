from google.oauth2 import service_account
from google.cloud import bigquery
from dotenv import load_dotenv
import json
import os

load_dotenv()

CREDS = os.getenv("CREDENTIALS")

if not CREDS:
    raise ValueError("Missing Google Credentials!")

try:
    CREDS_FILE = json.loads(CREDS)
except json.JSONDecodeError as e:
    raise ValueError("Invalid JSON in the credentials env file") from e

SCOPE = [
    'https://www.googleapis.com/auth/bigquery'
]

GOOGLE_CREDS = service_account.Credentials.from_service_account_info(
    CREDS_FILE,
    scopes=SCOPE
)

BQ_CLIENT = bigquery.Client(credentials=GOOGLE_CREDS, project=GOOGLE_CREDS.project_id)
PROJECT_ID = "mechanigo-liveagent"
DATASET_NAME = "conversations"