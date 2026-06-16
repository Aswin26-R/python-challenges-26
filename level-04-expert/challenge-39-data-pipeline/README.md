# Challenge 39: Data Pipeline

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 90 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to design data pipelines with clear Extract → Transform → Load (ETL) stages
- How to chain operations cleanly with functional programming
- How to process CSV data with the `csv` module
- How to aggregate and summarize datasets
- How to write pipeline stages that are composable and testable

---

## Problem Description

A **data pipeline** moves data from a source (Extract), transforms it (Transform), and loads it somewhere (Load). This is the core of data engineering.

In this challenge, you'll build a pipeline that reads a CSV of employee data, cleans it, filters it, and produces a summary report.

---

## Requirements

- [ ] `extract_csv(filepath)` — read CSV and return list of dicts
- [ ] `clean_record(record)` — normalize a single record (strip whitespace, fix types)
- [ ] `filter_records(records, **criteria)` — filter records by field values
- [ ] `transform_salaries(records, multiplier)` — multiply all salaries by a factor
- [ ] `aggregate_by_department(records)` — group records and compute dept stats
- [ ] `run_pipeline(filepath)` — run the full ETL pipeline and return summary

---

## Input Data Format (CSV)

```csv
name,department,salary,years
Alice,Engineering,95000,3
Bob,Marketing ,78000,7
  Charlie,Engineering,110000,5
Diana,HR,65000,2
```

---

## Expected Behavior

```python
# After extract + clean:
records = [
    {"name": "Alice", "department": "Engineering", "salary": 95000.0, "years": 3},
    {"name": "Bob", "department": "Marketing", "salary": 78000.0, "years": 7},
    ...
]

# Filter by department:
eng = filter_records(records, department="Engineering")
# Returns only Engineering employees

# Aggregate:
stats = aggregate_by_department(records)
# Returns:
# {
#   "Engineering": {"count": 2, "avg_salary": 102500.0, "total_salary": 205000.0},
#   "Marketing":   {"count": 1, "avg_salary": 78000.0,  "total_salary": 78000.0},
#   ...
# }
```

---

## The ETL Pattern

```
Extract → Transform → Load

Extract:    Read raw data (CSV → list of dicts)
Transform:  Clean, filter, normalize, aggregate
Load:       Write to output (print, save to file, return summary)
```

---

## Hints

> **Hint 1:** `extract_csv` uses `csv.DictReader`. Each row comes out as a dict with string values.

> **Hint 2:** `clean_record` should: strip whitespace from all string values, convert `salary` to `float`, convert `years` to `int`.

> **Hint 3:** `filter_records(records, department="Engineering")` checks each record: does `record[key] == value` for all keyword args?

> **Hint 4:** `aggregate_by_department`: group by `department`, then compute count, sum, and average of salaries for each group.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-39-data-pipeline
pytest tests/ -v
```
