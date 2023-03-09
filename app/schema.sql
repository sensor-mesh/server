DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS node;
DROP TABLE IF EXISTS data;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE node (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  type TEXT NOT NULL,
  active INTEGER DEFAULT 0
);

CREATE TABLE data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  payload TEXT,
  node_id INTEGER,
  FOREIGN KEY (node_id) REFERENCES node (id)
)