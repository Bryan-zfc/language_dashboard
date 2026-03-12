from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database connection
def get_db():
    return sqlite3.connect("study.db")

# Pydantic model for incoming JSON SESSION
class Session(BaseModel):
    language: str
    skill: str
    activity: str
    study_date: str           # format YYYY-MM-DD
    duration_minutes: int

# POST endpoint
@app.post("/add_session")
def add_session(session: Session):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sessions (language, skill, activity, study_date, duration_minutes)
    VALUES (?, ?, ?, ?, ?)
    """, (session.language, session.skill, session.activity, session.study_date, session.duration_minutes))

    conn.commit()
    conn.close()

    return {"message": "Session added"}

# GET endpoint
@app.get("/sessions")
def get_sessions():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT language, skill, activity, study_date, duration_minutes FROM sessions")
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


# Adding books read on backend
# Pydantic model for incoming JSON BOOKS
class Book(BaseModel):
    title : str
    author : str
    language: str
    pages: int
    finish_date: str           # format YYYY-MM-DD

# POST endpoint
@app.post("/add_book")
def add_book(book: Book):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books (title, author, language, pages, finish_date)
    VALUES (?, ?, ?, ?, ?)
    """, (book.title, book.author, book.language, book.pages, book.finish_date))

    conn.commit()
    conn.close()

    return {"message": "Book added"}

@app.get("/books")
def get_books():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT title, author, language, pages, finish_date
    FROM books
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows




# Remove the databases

@app.delete("/sessions")
def delete_all_sessions():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions")  # removes all rows
    conn.commit()
    conn.close()
    return {"message": "All sessions deleted"}


@app.delete("/books")
def delete_all_books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books")  # removes all rows
    conn.commit()
    conn.close()
    return {"message": "All books deleted"}


