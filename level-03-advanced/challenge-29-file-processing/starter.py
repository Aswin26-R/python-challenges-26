import csv
import os


def write_file(filepath, content):
    """
    TODO:
    Write the content string to the file at filepath.
    Create the file if it doesn't exist, overwrite if it does.

    Examples:
        write_file("test.txt", "Hello World")
        write_file("test.txt", "Line 1\nLine 2\n")

    Hint:
        with open(filepath, "w") as f:
            f.write(content)
    """
    pass


def read_file(filepath):
    """
    TODO:
    Read and return the entire contents of the file at filepath as a string.

    Examples:
        content = read_file("test.txt")
        # Returns: "Hello World"

    Hint:
        with open(filepath, "r") as f:
            return f.read()
    """
    pass


def count_lines(filepath):
    """
    TODO:
    Return the number of non-empty lines in the file.
    A line is empty if it contains only whitespace or nothing.

    Examples:
        # If test.txt contains "Hello\nWorld\n":
        count_lines("test.txt")  → 2

        # If test.txt contains "Line 1\nLine 2\nLine 3":
        count_lines("test.txt")  → 3

    Hint:
        Read all lines with f.readlines() or f.read().split('\n')
        Count only non-empty lines: [line for line in lines if line.strip()]
    """
    pass


def write_csv(filepath, headers, rows):
    """
    TODO:
    Write a CSV file with the given headers and rows.

    Parameters:
        filepath — path to the CSV file to create
        headers  — list of column names: ["name", "age", "city"]
        rows     — list of lists, each a data row: [["Alice", "30", "NYC"], ...]

    Hint:
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for row in rows:
                writer.writerow(row)
    """
    pass


def read_csv(filepath):
    """
    TODO:
    Read a CSV file and return a list of dictionaries.
    Each dictionary represents one row, with column headers as keys.

    Example:
        # data.csv contains:
        # name,age
        # Alice,30
        # Bob,25

        read_csv("data.csv")
        → [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]

    Hint:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    """
    pass


def search_in_file(filepath, keyword):
    """
    TODO:
    Return a list of lines from the file that contain the keyword.
    Strip trailing whitespace from each line.

    Example:
        # test.txt contains:
        # Hello World
        # Python is great
        # Hello Python

        search_in_file("test.txt", "Hello")
        → ["Hello World", "Hello Python"]

        search_in_file("test.txt", "xyz")
        → []

    Hint:
        with open(filepath, "r") as f:
            lines = f.readlines()
        return [line.strip() for line in lines if keyword in line]
    """
    pass
