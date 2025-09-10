from google.cloud.exceptions import NotFound
from config import DATASET_NAME, BQ_CLIENT
from typing import Optional, List, Literal
from google.cloud import bigquery

import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BigQuery:
    def __init__(self, client: bigquery.Client = BQ_CLIENT):
        self.client = client
        self.dataset_id = DATASET_NAME

    def execute_query(self, query: str, return_data: bool = True) -> Optional[pd.DataFrame]:
        query_job = self.client.query(query)
        if return_data:
            df = query_job.to_dataframe()
            return df
        else:
            query_job.result()
            return None