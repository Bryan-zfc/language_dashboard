import streamlit as st
import requests
import pandas as pd
import datetime
import time 

st.title("Language Study Sessions")

#Fetch already existing languages
def fetch_languages():
    try:
        langs = requests.get("http://127.0.0.1:8000/languages").json()
    except:
        langs = []
    return langs

# Fetch languages every time before showing the dropdown
existing_languages = fetch_languages()

# Add an option at the top for typing a new language
existing_languages.append("Add new language...")  # empty string will allow typing new

# Single entry bar: select existing or type new
language = st.selectbox("Language (pick or type new)", existing_languages)

# If user picks the placeholder, force text input
if language == "Add new language...":
    language = st.text_input("Enter new language")

# Enforce mandatory language
if not language:
    st.warning("Please provide a language to log the session.")
    st.stop()  # stops execution until language is provided


# Other session details
skill = st.selectbox(
    "Skill",
    ["", "Reading", "Listening", "Speaking", "Writing"], )

if skill == "":
    st.stop()  # stops execution until skill is provided


duration = st.number_input("Minutes studied", 0, None)
if duration ==0:
    st.stop()  # stops execution until skill is provided


date = st.date_input("Study date", datetime.date.today())


activity = st.text_input("Activity (optional)")

if st.button("Log Study Session"):

    response = requests.post(
        "http://127.0.0.1:8000/add_session",
        json={
            "language": language,
            "skill": skill,
            "activity": activity,
            "study_date": str(date),
            "duration_minutes": duration
        }
    )
    if response.status_code == 200:
        st.success("Session recorded!")
        # add a small pause
        time.sleep(1)
        existing_languages = fetch_languages()
        st.rerun()
    else:
        st.error(f"Failed to log session: {response.status_code} {response.text}")



