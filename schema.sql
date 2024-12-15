CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, admin BOOLEAN);

CREATE TABLE messages (id SERIAL PRIMARY KEY, header TEXT, content TEXT, sent TIMESTAMP, votes INTEGER, user_id INTEGER REFERENCES users);



