import sqlite3


def create_database(db_path):
    """
    TODO:
    Create a SQLite database at db_path with a 'students' table.
    If the table already exists, do NOT recreate it (use IF NOT EXISTS).

    Schema:
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT    NOT NULL,
            grade TEXT    NOT NULL,
            score REAL    NOT NULL
        )

    Hint:
        with sqlite3.connect(db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS students (...)")
    """
    pass


def add_student(db_path, name, grade, score):
    """
    TODO:
    Insert a new student record into the database.
    Return the ID of the newly inserted student.

    Parameters:
        db_path — path to the .db file
        name    — student name (string)
        grade   — letter grade: "A", "B", "C", etc.
        score   — numeric score (float)

    Example:
        student_id = add_student("test.db", "Alice", "A", 95.0)
        # Returns: 1  (the auto-generated id)

    Hint:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO students (name, grade, score) VALUES (?, ?, ?)",
                (name, grade, score)
            )
            return cursor.lastrowid
    """
    pass


def get_student(db_path, student_id):
    """
    TODO:
    Retrieve a single student by their ID.
    Return a dict: {"id": ..., "name": ..., "grade": ..., "score": ...}
    Return None if no student found with that ID.

    Hint:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute("SELECT id, name, grade, score FROM students WHERE id = ?", (student_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return {"id": row[0], "name": row[1], "grade": row[2], "score": row[3]}
    """
    pass


def get_all_students(db_path):
    """
    TODO:
    Retrieve all students from the database.
    Return a list of dicts, each with keys: id, name, grade, score.
    Return [] if no students exist.

    Hint:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute("SELECT id, name, grade, score FROM students")
            rows = cursor.fetchall()
            return [{"id": r[0], "name": r[1], "grade": r[2], "score": r[3]} for r in rows]
    """
    pass


def update_score(db_path, student_id, new_score):
    """
    TODO:
    Update the score for a student with the given ID.
    Return True if student was found and updated, False otherwise.

    Hint:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute(
                "UPDATE students SET score = ? WHERE id = ?",
                (new_score, student_id)
            )
            return cursor.rowcount > 0
    """
    pass


def delete_student(db_path, student_id):
    """
    TODO:
    Delete the student with the given ID.
    Return True if deleted, False if student not found.

    Hint:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
            return cursor.rowcount > 0
    """
    pass


def get_students_by_grade(db_path, grade):
    """
    TODO:
    Return all students with the given grade.
    Return a list of dicts (same format as get_all_students).
    Return [] if none found.

    Hint:
        Same pattern as get_all_students but with WHERE grade = ?
    """
    pass


def get_average_score(db_path):
    """
    TODO:
    Return the average score of all students, rounded to 2 decimal places.
    Return None if there are no students.

    Hint:
        cursor = conn.execute("SELECT AVG(score) FROM students")
        avg = cursor.fetchone()[0]
        if avg is None:
            return None
        return round(avg, 2)
    """
    pass
