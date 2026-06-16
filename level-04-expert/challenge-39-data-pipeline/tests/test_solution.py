import pytest
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import (
    extract_csv, clean_record, filter_records,
    transform_salaries, aggregate_by_department, run_pipeline
)


@pytest.fixture
def sample_csv(tmp_path):
    filepath = str(tmp_path / "employees.csv")
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "department", "salary", "years"])
        writer.writerow(["Alice", "Engineering", "95000", "3"])
        writer.writerow(["Bob", "Marketing ", "78000", "7"])
        writer.writerow(["  Charlie", "Engineering", "110000", "5"])
        writer.writerow(["Diana", "HR", "65000", "2"])
    return filepath


@pytest.fixture
def clean_records():
    return [
        {"name": "Alice", "department": "Engineering", "salary": 95000.0, "years": 3},
        {"name": "Bob", "department": "Marketing", "salary": 78000.0, "years": 7},
        {"name": "Charlie", "department": "Engineering", "salary": 110000.0, "years": 5},
        {"name": "Diana", "department": "HR", "salary": 65000.0, "years": 2},
    ]


class TestExtractCsv:
    def test_returns_list(self, sample_csv):
        result = extract_csv(sample_csv)
        assert isinstance(result, list)

    def test_returns_dicts(self, sample_csv):
        result = extract_csv(sample_csv)
        assert all(isinstance(r, dict) for r in result)

    def test_correct_count(self, sample_csv):
        result = extract_csv(sample_csv)
        assert len(result) == 4

    def test_missing_file_returns_empty(self, tmp_path):
        result = extract_csv(str(tmp_path / "nonexistent.csv"))
        assert result == []


class TestCleanRecord:
    def test_strips_whitespace_from_name(self):
        record = {"name": "  Alice ", "department": "Engineering", "salary": "95000", "years": "3"}
        cleaned = clean_record(record)
        assert cleaned["name"] == "Alice"

    def test_strips_whitespace_from_department(self):
        record = {"name": "Bob", "department": "Marketing ", "salary": "78000", "years": "7"}
        cleaned = clean_record(record)
        assert cleaned["department"] == "Marketing"

    def test_converts_salary_to_float(self):
        record = {"name": "Alice", "department": "Eng", "salary": "95000", "years": "3"}
        cleaned = clean_record(record)
        assert isinstance(cleaned["salary"], float)
        assert cleaned["salary"] == 95000.0

    def test_converts_years_to_int(self):
        record = {"name": "Alice", "department": "Eng", "salary": "95000", "years": "3"}
        cleaned = clean_record(record)
        assert isinstance(cleaned["years"], int)
        assert cleaned["years"] == 3

    def test_does_not_modify_original(self):
        record = {"name": "Alice", "department": "Eng", "salary": "95000", "years": "3"}
        original_salary = record["salary"]
        clean_record(record)
        assert record["salary"] == original_salary


class TestFilterRecords:
    def test_filter_by_department(self, clean_records):
        result = filter_records(clean_records, department="Engineering")
        assert len(result) == 2
        assert all(r["department"] == "Engineering" for r in result)

    def test_filter_no_match(self, clean_records):
        result = filter_records(clean_records, department="Finance")
        assert result == []

    def test_filter_multiple_criteria(self, clean_records):
        result = filter_records(clean_records, department="Engineering", years=3)
        assert len(result) == 1
        assert result[0]["name"] == "Alice"

    def test_no_filter_returns_all(self, clean_records):
        result = filter_records(clean_records)
        assert len(result) == 4


class TestTransformSalaries:
    def test_multiplies_salaries(self, clean_records):
        result = transform_salaries(clean_records, 1.1)
        assert result[0]["salary"] == round(95000.0 * 1.1, 2)

    def test_does_not_modify_original(self, clean_records):
        original_salary = clean_records[0]["salary"]
        transform_salaries(clean_records, 2.0)
        assert clean_records[0]["salary"] == original_salary

    def test_returns_new_list(self, clean_records):
        result = transform_salaries(clean_records, 1.0)
        assert result is not clean_records


class TestAggregateByDepartment:
    def test_groups_by_department(self, clean_records):
        result = aggregate_by_department(clean_records)
        assert "Engineering" in result
        assert "Marketing" in result
        assert "HR" in result

    def test_engineering_count(self, clean_records):
        result = aggregate_by_department(clean_records)
        assert result["Engineering"]["count"] == 2

    def test_engineering_avg_salary(self, clean_records):
        result = aggregate_by_department(clean_records)
        expected = round((95000.0 + 110000.0) / 2, 2)
        assert result["Engineering"]["avg_salary"] == expected

    def test_total_salary(self, clean_records):
        result = aggregate_by_department(clean_records)
        assert result["Engineering"]["total_salary"] == 205000.0


class TestRunPipeline:
    def test_returns_dict(self, sample_csv):
        result = run_pipeline(sample_csv)
        assert isinstance(result, dict)

    def test_total_records(self, sample_csv):
        result = run_pipeline(sample_csv)
        assert result["total_records"] == 4

    def test_departments_present(self, sample_csv):
        result = run_pipeline(sample_csv)
        assert "departments" in result
        assert "Engineering" in result["departments"]

    def test_cleans_data(self, sample_csv):
        result = run_pipeline(sample_csv)
        # After cleaning, salaries should be floats not strings
        eng = result["departments"]["Engineering"]
        assert isinstance(eng["avg_salary"], float)
