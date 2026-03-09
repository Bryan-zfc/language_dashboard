import streamlit as st
import requests
import pandas as pd
import datetime

st.title("Language Study Dashboard")

try:
    existing_languages = requests.get("http://127.0.0.1:8000/languages").json()
except:
    existing_languages = []

# Add an option at the top for typing a new language
existing_languages.insert(0, "")  # empty string will allow typing new

# Single entry bar: select existing or type new
language = st.selectbox("Language (pick or type new)", existing_languages)
if language == "":
    language = st.text_input("Enter new language")

skill = st.selectbox(
    "Skill",
    ["Reading", "Listening", "Speaking", "Writing"]
)

duration = st.number_input("Minutes studied", 0, 300)
date = st.date_input("Study date", datetime.date.today())

if st.button("Log Study Session"):

    requests.post(
        "http://127.0.0.1:8000/add_session",
        json={
            "language": language,
            "skill": skill,
            "study_date": str(date),
            "duration_minutes": duration
        }
    )
    st.success("Session recorded!")

    st.rerun()  



data = requests.get("http://127.0.0.1:8000/sessions").json()

df = pd.DataFrame(data, columns=["language", "skill", "date", "minutes"])

st.subheader("Study Sessions")

st.dataframe(df)

st.subheader("Total Study Time by Language")

chart = df.groupby("language")["minutes"].sum()

st.bar_chart(chart)

# How to run: cd language_dashboard
# First run front end in terminal: uvicorn backend.server:app --reload
# Run frontend in new terminal: streamlit run frontend/dashboard.py
