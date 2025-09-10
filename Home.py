from config import PROJECT_ID, DATASET_NAME
from BigQuery import BigQuery
import streamlit as st

def get_convo_data(ticket_id: str):
    bq = BigQuery()
    query = """
    SELECT
    sender_type, receiver_type, message, message_datecreated
    FROM `{}.{}.messages`
    WHERE ticket_id = '{}'
    AND message_type = 'M' AND message_format = 'T'
    ORDER BY message_datecreated ASC
    """.format(PROJECT_ID, DATASET_NAME, ticket_id)

    return bq.execute_query(query)

st.set_page_config(
    page_title="MGO Conversation Viewer",
    page_icon="💬",
    layout="wide"
)

with st.container(border=True):
    st.title("MehaniGo.ph Conversation Viewer")
    st.caption("Enter the Ticket ID to view the conversation data.")

with st.form("convo_viewer"):
    ticket_id = st.text_input("Ticket ID:")
    search = st.form_submit_button("Search")

    if search:
        with st.spinner("Searching..."):
            df = get_convo_data(ticket_id)

        if df is not None and not df.empty:
            st.success(f"Found {len(df)} messages.")
            st.dataframe(df, hide_index=True)
        else:
            st.warning("No data found!")