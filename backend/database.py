import sqlite3

conn = sqlite3.connect("study.db")

with open("database/schema.sql") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully")
