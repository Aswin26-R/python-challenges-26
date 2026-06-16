import csv
import os


def extract_csv(filepath):
    """
    TODO:
    Read a CSV file and return a list of dicts.
    Each row becomes a dict with column headers as keys.
    Returns [] if file doesn't exist.

    Example (given a CSV with columns name, department, salary, years):
        [
            {"name": "  Alice", "department": "Engineering", "salary": "95000", "years": "3"},
            ...
        ]

    Note: ALL values are strings at this stage. Cleaning happens next.

    Hint:
        if not os.path.exists(filepath):
            return []
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    """
    pass


def clean_record(record):
    """
    TODO:
    Clean and normalize a single record dict.
    Return a new cleaned dict (don't modify original).

    Cleaning steps:
        1. Strip leading/trailing whitespace from ALL string values AND keys
        2. Convert "salary" value to float
        3. Convert "years" value to int

    Example:
        clean_record({"name": "  Alice ", "department": "Engineering ", "salary": "95000", "years": "3"})
        → {"name": "Alice", "department": "Engineering", "salary": 95000.0, "years": 3}

    Hint:
        cleaned = {k.strip(): v.strip() if isinstance(v, str) else v for k, v in record.items()}
        cleaned["salary"] = float(cleaned["salary"])
        cleaned["years"] = int(cleaned["years"])
        return cleaned
    """
    pass


def filter_records(records, **criteria):
    """
    TODO:
    Filter a list of records by field values.
    Keep records where ALL criteria match.

    Example:
        filter_records(records, department="Engineering")
        → only Engineering records

        filter_records(records, department="Engineering", years=3)
        → Engineering records where years == 3

    Hint:
        return [
            r for r in records
            if all(r.get(key) == value for key, value in criteria.items())
        ]
    """
    pass


def transform_salaries(records, multiplier):
    """
    TODO:
    Return a new list of records with each salary multiplied by 'multiplier'.
    Don't modify the original records.

    Example:
        transform_salaries(records, 1.1)
        → all salaries increased by 10%

    Hint:
        return [{**r, "salary": round(r["salary"] * multiplier, 2)} for r in records]
    """
    pass


def aggregate_by_department(records):
    """
    TODO:
    Group records by department and compute statistics.
    Return a dict: {department_name: {count, avg_salary, total_salary}}

    Example:
        {
            "Engineering": {
                "count": 2,
                "total_salary": 205000.0,
                "avg_salary": 102500.0
            },
            "Marketing": {
                "count": 1,
                "total_salary": 78000.0,
                "avg_salary": 78000.0
            }
        }

    Hint:
        groups = {}
        for record in records:
            dept = record["department"]
            if dept not in groups:
                groups[dept] = []
            groups[dept].append(record["salary"])

        result = {}
        for dept, salaries in groups.items():
            total = sum(salaries)
            result[dept] = {
                "count": len(salaries),
                "total_salary": total,
                "avg_salary": round(total / len(salaries), 2)
            }
        return result
    """
    pass


def run_pipeline(filepath):
    """
    TODO:
    Run the full ETL pipeline:
        1. Extract: extract_csv(filepath)
        2. Transform: clean each record with clean_record()
        3. Aggregate: aggregate_by_department()

    Return a dict:
        {
            "total_records": <int>,
            "departments": <result of aggregate_by_department>
        }

    Example:
        result = run_pipeline("employees.csv")
        result["total_records"]  → 4
        result["departments"]["Engineering"]["count"]  → 2
    """
    pass
