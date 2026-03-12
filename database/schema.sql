
-- Create a table with all study sessions

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT NOT NULL, -- Which Language
    skill TEXT NOT NULL, -- Which skill (speaking, listening, reading, writing),
    activity TEXT,
    study_date DATE,
    duration_minutes INTEGER
);

-- Create a table with all read books

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL, 
    author TEXT NOT NULL,
    language TEXT NOT NULL,
    pages INTEGER,
    finish_date DATE
);
