# How to run:
# First run back end in terminal: uvicorn backend.server:app --reload
# Run frontend in new terminal: streamlit run frontend/dashboard.py

import streamlit as st
import requests
import pandas as pd

st.title("Language Study Dashboard")

data = requests.get("http://127.0.0.1:8000/sessions").json()

df = pd.DataFrame(
    data,
    columns=["language", "skill", "activity","study_date","duration_minutes"]
)

st.subheader("Study Sessions")

with st.expander("Click to see all study sessions"):
    st.dataframe(df, 
            hide_index=True,
            column_config={
                "language": st.column_config.Column(
             label="Language", # The label shown in the UI
             width="small"
             ),

            "skill": st.column_config.Column(
             label="Skill", # The label shown in the UI
             width="small",
             help="Which language skill have you trained"
             ),

             "activity": st.column_config.Column(
             label="Activity", # The label shown in the UI
             width="medium",
             help="What did you do this learning session?"
             ),

            "study_date": st.column_config.Column(
             label="Study Date", # The label shown in the UI
             width="small"
             ),
            "duration_minutes": st.column_config.Column(
             label="Session Duration", # The label shown in the UI
             width="small",
             ),
            
            }       
    )


# Show a barchart with the total hours studied per language
st.subheader("Total Study Time by Language")

chart = df.groupby("language")["duration_minutes"].sum() /60
st.bar_chart(chart, y_label = "Total Hours")


# Show a table with all the read books
data_books = requests.get("http://127.0.0.1:8000/books").json()

df = pd.DataFrame(data_books, columns=["title", "author", "language", "pages", "finish_date"])

st.subheader("Finished Books")

st.dataframe(df)

st.subheader("Total pages read by Language")

chart = df.groupby("language")["pages"].sum()

st.bar_chart(chart)
