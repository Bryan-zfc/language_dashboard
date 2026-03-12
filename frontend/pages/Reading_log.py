import streamlit as st
import requests
import pandas as pd
import datetime
import time

st.title("Finished books")

try:
    existing_languages = requests.get("http://127.0.0.1:8000/languages").json()
except:
    existing_languages = []



title = st.text_input("Title")
author = st.text_input("Author")
if author == "" or title == "":
    st.stop()  # stops execution until title and author are provided

existing_languages.insert(0, "")
language = st.selectbox("Language", existing_languages)
if language  == "":
    st.stop()  # stops execution until title and author are provided

pages = st.number_input("Pages", 0, None)
if pages == 0:
    st.stop() # stops execution until the number of pages is supplied

date = st.date_input("Finish date", datetime.date.today())

if st.button("Log book"):

    response = requests.post(
        "http://127.0.0.1:8000/add_book",
        json={
            "title": title,
            "author": author,
            "language": language,
            "pages": pages,
            "finish_date": str(date)
        }
    )



    if response.status_code == 200:
        st.success("Book logged!")
        time.sleep(1)
        st.rerun()



response = requests.get("http://127.0.0.1:8000/books")

if response.status_code == 200:
    data = response.json()
else:
    st.error(f"Backend error: {response.status_code}")
    st.write(response.text)  # shows the real backend error
    st.stop()

