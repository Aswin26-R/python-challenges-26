# Challenge 29: File Processing

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 65 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to read and write files in Python
- How to use the `csv` module to parse CSV data
- How to process data from files
- How to use `os.path` for file operations

---

## Problem Description

Reading and writing files is fundamental to real-world programming. You will write functions that process text files and CSV files — tasks that appear constantly in data engineering, backend development, and scripting.

---

## Requirements

- [ ] `write_file(filepath, content)` — writes content to a file
- [ ] `read_file(filepath)` — reads and returns the file contents
- [ ] `count_lines(filepath)` — counts lines in a file
- [ ] `write_csv(filepath, headers, rows)` — writes a CSV file
- [ ] `read_csv(filepath)` — reads a CSV and returns a list of dicts
- [ ] `search_in_file(filepath, keyword)` — returns lines containing the keyword

---

## Expected Behavior

```python
write_file("test.txt", "Hello\nWorld\n")
read_file("test.txt")
# Returns: "Hello\nWorld\n"

count_lines("test.txt")
# Returns: 2

write_csv("data.csv",
    headers=["name", "age"],
    rows=[["Alice", "30"], ["Bob", "25"]]
)
read_csv("data.csv")
# Returns: [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]

search_in_file("test.txt", "Hello")
# Returns: ["Hello"]
```

---

## File Opening Modes

```python
open("file.txt", "r")   # read (default)
open("file.txt", "w")   # write (creates/overwrites)
open("file.txt", "a")   # append (adds to end)
```

Always use `with open(...) as f:` — this ensures the file is closed even if an error occurs.

---

## CSV Module

```python
import csv

# Writing CSV:
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])   # header
    writer.writerow(["Alice", "30"])   # data row

# Reading CSV as dicts:
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)   # {"name": "Alice", "age": "30"}
```

---

## Hints

> **Hint 1:** `write_file`: `with open(filepath, "w") as f: f.write(content)`.

> **Hint 2:** `read_file`: `with open(filepath, "r") as f: return f.read()`.

> **Hint 3:** `count_lines`: read the file, split by newlines. Be careful: a trailing newline creates an empty string at the end.

> **Hint 4:** `read_csv`: use `csv.DictReader`. Convert the reader to a list: `list(reader)`.

> **Hint 5:** `search_in_file`: read all lines, filter those containing the keyword.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-29-file-processing
pytest tests/ -v
```
