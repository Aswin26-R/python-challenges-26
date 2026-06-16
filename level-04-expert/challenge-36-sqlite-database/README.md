# Challenge 36: SQLite Database

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 90 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to work with SQLite — a lightweight database built into Python
- SQL fundamentals: CREATE TABLE, INSERT, SELECT, UPDATE, DELETE
- How to use `sqlite3` module for database operations
- How to use parameterized queries to prevent SQL injection
- Database design and CRUD operations

---

## Problem Description

SQLite is a fully-featured database engine built into Python. No setup required — just `import sqlite3`. In this challenge, you'll build a simple student database with full CRUD operations.

---

## Requirements

- [ ] `create_database(db_path)` — create database and students table
- [ ] `add_student(db_path, name, grade, score)` — insert a student record
- [ ] `get_student(db_path, student_id)` — retrieve student by ID
- [ ] `get_all_students(db_path)` — retrieve all students
- [ ] `update_score(db_path, student_id, new_score)` — update student's score
- [ ] `delete_student(db_path, student_id)` — delete student record
- [ ] `get_students_by_grade(db_path, grade)` — filter students by grade
- [ ] `get_average_score(db_path)` — compute average score of all students

---

## Database Schema

```sql
CREATE TABLE students (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    grade TEXT    NOT NULL,
    score REAL    NOT NULL
)
```

---

## Expected Behavior

```python
db = "test.db"
create_database(db)

add_student(db, "Alice", "A", 95.0)
add_student(db, "Bob", "B", 78.5)
add_student(db, "Charlie", "A", 88.0)

get_all_students(db)
# Returns: [
#   {"id": 1, "name": "Alice", "grade": "A", "score": 95.0},
#   {"id": 2, "name": "Bob",   "grade": "B", "score": 78.5},
#   {"id": 3, "name": "Charlie", "grade": "A", "score": 88.0},
# ]

get_student(db, 1)
# Returns: {"id": 1, "name": "Alice", "grade": "A", "score": 95.0}

get_students_by_grade(db, "A")
# Returns: [Alice, Charlie]

get_average_score(db)
# Returns: 87.17  (rounded to 2 decimal places)

update_score(db, 2, 82.0)
delete_student(db, 3)
```

---

## sqlite3 Basics

```python
import sqlite3

# Connect (creates file if it doesn't exist):
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Execute SQL:
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Insert (use ? placeholders — NEVER f-strings for SQL!):
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
conn.commit()   # save changes

# Query:
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
row = cursor.fetchone()   # one row
rows = cursor.fetchall()  # all rows

conn.close()
```

---

## Hints

> **Hint 1:** Always use `?` placeholders for values, never string formatting. SQL injection is a real vulnerability.

> **Hint 2:** Use `conn.row_factory = sqlite3.Row` to get dict-like rows, OR convert manually: `{"id": row[0], "name": row[1], ...}`.

> **Hint 3:** `get_average_score` can use SQL: `SELECT AVG(score) FROM students`.

> **Hint 4:** Use `with sqlite3.connect(db_path) as conn:` — this auto-commits on success and auto-rolls back on error.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-36-sqlite-database
pytest tests/ -v
```
