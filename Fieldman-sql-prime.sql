-----------------------------------
-------  SQL FIELD MANUAL  --------
-----------------------------------

-- Usefull stuff:
-- https://www.sqlite.org/about.html
-- https://dbfiddle.uk/
-- DBBrowser for SQLite

-- This is a comment
-- Every query must end with semicolon `;`
CREATE TABLE agents (name TEXT, special_number INTEGER);
CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT);

-- Single quotes vs Double quotes:
-- [S]ingle quotes are for [S]trings Literals (date literals are also strings)
-- [D]ouble quotes are for [D]atabase Identifiers

-- https://www.sqlite.org/lang_insert.html
INSERT INTO agents (name, special_number) VALUES ('Smith', 8000), ('John', 7000);

-- https://www.sqlite.org/lang_select.html
SELECT name, special_number FROM agents;
SELECT * FROM books;

SELECT DISTINCT name, special_number
FROM agents
WHERE (special_number  = 1000 OR special_number >= 2000) AND name != 'Smith'
ORDER BY special_number DESC
LIMIT 10;

-- Wildcards; LIKE
-- Useful for search queries
SELECT * FROM books
WHERE title LIKE 'Ha%'
-- Wildcards: `%` any amount of characters; `_` single character

-- `=` is overloaded for assignment
UPDATE books SET title = 'Title', author = 'Author' WHERE author = 'Someone';

DELETE FROM books WHERE title = 'Harry Potter'; -- delete whole rows
-- Note: WHERE section is VERY important, or it will delete everything.

DROP TABLE IF EXISTS agents;

-- Primary and Foreign Keys declaraion
CREATE TABLE users (
    id INTEGER PRIMARY KEY, -- aliased to rowid (row identifier); autoincrementing
    first_name TEXT,
    last_name TEXT
    -- PRIMARY KEY(id) -- also possible
);

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    holder_id INTEGER, -- is foreign key
    number TEXT,
    FOREIGN KEY(holder_id) REFERENCES users(id) -- helps db engine to perform checks
);

-- Join
SELECT users.*, id
FROM users
JOIN accounts -- inner join
ON users.id = accounts.holeder_id
WHERE users.last_name = 'Anderson';

-- Index tree
-- Balanced B-tree, used for fast search of rows
-- Index makes read queries faster (O(logn) instead O(n)),
-- Index makes writing slower (need to move tree branches)
-- Also uses additional storage space (is a table)
CREATE INDEX IF NOT EXISTS idx_books_author ON books(author)
-- will speed up author-related queries


-- Virtual table. Create temporary table (Joins) for future usage.
-- Window Over-function. Used for calculating new generated values for selects
--  also can use previous/next rows
--  similar to QlikView ROW_NUMBER As number.

