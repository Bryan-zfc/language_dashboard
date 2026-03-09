CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT NOT NULL, -- Which Language
    skill TEXT NOT NULL, -- Which skill (speaking, listening, reading, writing)
    study_date DATE,
    duration_minutes INTEGER
);
