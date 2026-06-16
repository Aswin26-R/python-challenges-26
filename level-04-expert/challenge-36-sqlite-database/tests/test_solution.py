import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import (
    create_database, add_student, get_student, get_all_students,
    update_score, delete_student, get_students_by_grade, get_average_score
)


@pytest.fixture
def db(tmp_path):
    db_path = str(tmp_path / "test.db")
    create_database(db_path)
    return db_path


@pytest.fixture
def populated_db(db):
    add_student(db, "Alice", "A", 95.0)
    add_student(db, "Bob", "B", 78.5)
    add_student(db, "Charlie", "A", 88.0)
    return db


class TestCreateDatabase:
    def test_creates_file(self, tmp_path):
        db_path = str(tmp_path / "new.db")
        create_database(db_path)
        assert os.path.exists(db_path)

    def test_idempotent(self, tmp_path):
        db_path = str(tmp_path / "new.db")
        create_database(db_path)
        create_database(db_path)  # calling twice should not raise


class TestAddStudent:
    def test_returns_id(self, db):
        student_id = add_student(db, "Alice", "A", 95.0)
        assert student_id == 1

    def test_ids_increment(self, db):
        id1 = add_student(db, "Alice", "A", 95.0)
        id2 = add_student(db, "Bob", "B", 78.5)
        assert id2 == id1 + 1

    def test_returns_integer(self, db):
        result = add_student(db, "Alice", "A", 95.0)
        assert isinstance(result, int)


class TestGetStudent:
    def test_get_existing(self, populated_db):
        student = get_student(populated_db, 1)
        assert student["name"] == "Alice"
        assert student["grade"] == "A"
        assert student["score"] == 95.0

    def test_get_returns_dict(self, populated_db):
        student = get_student(populated_db, 1)
        assert isinstance(student, dict)
        assert "id" in student and "name" in student

    def test_get_missing_returns_none(self, populated_db):
        assert get_student(populated_db, 999) is None


class TestGetAllStudents:
    def test_returns_all(self, populated_db):
        students = get_all_students(populated_db)
        assert len(students) == 3

    def test_empty_db(self, db):
        assert get_all_students(db) == []

    def test_returns_list_of_dicts(self, populated_db):
        students = get_all_students(populated_db)
        assert isinstance(students, list)
        assert all(isinstance(s, dict) for s in students)


class TestUpdateScore:
    def test_updates_score(self, populated_db):
        update_score(populated_db, 1, 99.0)
        student = get_student(populated_db, 1)
        assert student["score"] == 99.0

    def test_returns_true_on_success(self, populated_db):
        assert update_score(populated_db, 1, 99.0) is True

    def test_returns_false_on_missing(self, populated_db):
        assert update_score(populated_db, 999, 99.0) is False


class TestDeleteStudent:
    def test_deletes_student(self, populated_db):
        delete_student(populated_db, 1)
        assert get_student(populated_db, 1) is None

    def test_returns_true_on_success(self, populated_db):
        assert delete_student(populated_db, 1) is True

    def test_returns_false_on_missing(self, populated_db):
        assert delete_student(populated_db, 999) is False

    def test_count_decreases(self, populated_db):
        delete_student(populated_db, 1)
        assert len(get_all_students(populated_db)) == 2


class TestGetStudentsByGrade:
    def test_filter_by_grade(self, populated_db):
        grade_a = get_students_by_grade(populated_db, "A")
        names = [s["name"] for s in grade_a]
        assert "Alice" in names
        assert "Charlie" in names
        assert "Bob" not in names

    def test_no_match_returns_empty(self, populated_db):
        assert get_students_by_grade(populated_db, "F") == []


class TestGetAverageScore:
    def test_computes_average(self, populated_db):
        avg = get_average_score(populated_db)
        expected = round((95.0 + 78.5 + 88.0) / 3, 2)
        assert avg == expected

    def test_empty_returns_none(self, db):
        assert get_average_score(db) is None

    def test_rounded_to_2_decimals(self, populated_db):
        avg = get_average_score(populated_db)
        assert isinstance(avg, float)
        assert avg == round(avg, 2)
