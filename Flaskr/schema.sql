DROP TABLE IF EXISTS picture;

CREATE TABLE picture (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);