CREATE TABLE users (name STRING PRIMARY KEY, checked_in BOOLEAN DEFAULT (0), checked_in_at DATETIME DEFAULT (CURRENT_TIMESTAMP), shirt_size STRING);
