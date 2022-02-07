-----------------------------------
-------  SQL FIELD MANUAL  --------
-----------------------------------

-- Usefull stuff:
-- https://www.sqlite.org/about.html
-- https://dbfiddle.uk/
-- DBBrowser for SQLite

-- This is a comment
-- Every query must end with semicolon `;`
CREATE TABLE  agents (name TEXT, special_number INTEGER);
CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT);

-- Single quotes vs Double quotes:
-- [S]ingle quotes are for [S]trings Literals (date literals are also strings)
-- [D]ouble quotes are for [D]atabase Identifiers

-- https://www.sqlite.org/lang_insert.html
INSERT INTO agents (name, special_number) VALUES ('Smith', 8000);

-- https://www.sqlite.org/lang_select.html
SELECT name, special_number FROM agents;
SELECT * FROM books;

SELECT name, special_number
FROM agents
WHERE (special_number  = 1000 OR special_number >= 2000) AND name != 'Smith'
ORDER BY special_number;

DROP TABLE IF EXISTs agents;
