from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database connection
def get_db():
    return sqlite3.connect("study.db")

# Pydantic model for incoming JSON
class Session(BaseModel):
    language: str
    skill: str
    study_date: str           # format YYYY-MM-DD
    duration_minutes: int

# POST endpoint
@app.post("/add_session")
def add_session(session: Session):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sessions (language, skill, study_date, duration_minutes)
    VALUES (?, ?, ?, ?)
    """, (session.language, session.skill, session.study_date, session.duration_minutes))

    conn.commit()
    conn.close()

    return {"message": "Session added"}

# GET endpoint
@app.get("/sessions")
def get_sessions():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT language, skill, study_date, duration_minutes FROM sessions")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/languages")
def get_languages():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT language FROM sessions")
    rows = cursor.fetchall()
    conn.close()
    # Flatten tuples
    return [row[0] for row in rows]


@app.delete("/sessions")
def delete_all_sessions():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions")  # removes all rows
    conn.commit()
    conn.close()
    return {"message": "All sessions deleted"}