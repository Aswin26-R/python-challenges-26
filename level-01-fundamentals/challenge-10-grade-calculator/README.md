# Challenge 10: Grade Calculator

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐⭐ (Beginner)
**Estimated Time:** 35 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to calculate averages
- How to use dictionaries to store related data
- How to convert numeric scores to letter grades
- How to write a function that returns a dictionary

---

## Problem Description

You are building a grade calculator for a student management system. Given a list of numeric scores, your functions should calculate the average and determine the letter grade.

---

## Requirements

- [ ] `calculate_average(scores)` — returns the average of a list of numbers (rounded to 2 decimal places)
- [ ] `get_letter_grade(score)` — returns the letter grade for a numeric score
- [ ] `create_report(student_name, scores)` — returns a dictionary with student information

---

## Grading Scale

| Score Range | Letter Grade |
|-------------|-------------|
| 90 – 100 | A |
| 80 – 89 | B |
| 70 – 79 | C |
| 60 – 69 | D |
| 0 – 59 | F |

---

## Expected Behavior

```python
calculate_average([90, 85, 92, 88])
# Returns: 88.75

calculate_average([100, 0])
# Returns: 50.0

get_letter_grade(95)
# Returns: "A"

get_letter_grade(85)
# Returns: "B"

get_letter_grade(72)
# Returns: "C"

get_letter_grade(65)
# Returns: "D"

get_letter_grade(45)
# Returns: "F"

create_report("Alice", [90, 85, 92])
# Returns: {
#     "name": "Alice",
#     "scores": [90, 85, 92],
#     "average": 89.0,
#     "grade": "B"
# }
```

---

## About Dictionaries

A dictionary stores key-value pairs:

```python
student = {
    "name": "Alice",
    "average": 89.0,
    "grade": "B"
}

student["name"]     # "Alice"
student["average"]  # 89.0
```

---

## Hints

> **Hint 1:** To calculate an average: `sum(scores) / len(scores)`.

> **Hint 2:** To round to 2 decimal places: `round(value, 2)`.

> **Hint 3:** For `get_letter_grade()`, use `if/elif/else` starting from the highest score down.

> **Hint 4:** For `create_report()`, build a dictionary: `{"name": student_name, "scores": scores, ...}`.

> **Hint 5:** In `create_report()`, call your other two functions to get the average and grade — don't duplicate logic.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-10-grade-calculator
pytest tests/ -v
```
