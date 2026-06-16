import pytest
import os
import tempfile
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import write_file, read_file, count_lines, write_csv, read_csv, search_in_file


@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path


class TestWriteAndReadFile:
    def test_write_creates_file(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Hello World")
        assert os.path.exists(path)

    def test_write_then_read(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Hello World")
        content = read_file(path)
        assert content == "Hello World"

    def test_write_multiline(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Line 1\nLine 2\nLine 3\n")
        content = read_file(path)
        assert "Line 1" in content
        assert "Line 2" in content

    def test_overwrite_existing(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "old content")
        write_file(path, "new content")
        content = read_file(path)
        assert content == "new content"


class TestCountLines:
    def test_two_lines(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Hello\nWorld\n")
        assert count_lines(path) == 2

    def test_three_lines(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Line 1\nLine 2\nLine 3")
        assert count_lines(path) == 3

    def test_single_line(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Hello")
        assert count_lines(path) == 1


class TestWriteReadCSV:
    def test_write_and_read_csv(self, temp_dir):
        path = str(temp_dir / "data.csv")
        write_csv(path, ["name", "age"], [["Alice", "30"], ["Bob", "25"]])
        rows = read_csv(path)
        assert len(rows) == 2
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "30"
        assert rows[1]["name"] == "Bob"

    def test_read_csv_returns_list_of_dicts(self, temp_dir):
        path = str(temp_dir / "data.csv")
        write_csv(path, ["x", "y"], [["1", "2"]])
        rows = read_csv(path)
        assert isinstance(rows, list)
        assert isinstance(rows[0], dict)

    def test_headers_become_keys(self, temp_dir):
        path = str(temp_dir / "data.csv")
        write_csv(path, ["col1", "col2"], [["a", "b"]])
        rows = read_csv(path)
        assert "col1" in rows[0]
        assert "col2" in rows[0]


class TestSearchInFile:
    def test_finds_matching_lines(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Hello World\nPython is great\nHello Python\n")
        result = search_in_file(path, "Hello")
        assert "Hello World" in result
        assert "Hello Python" in result

    def test_no_matches_returns_empty(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "Hello\nWorld\n")
        result = search_in_file(path, "xyz")
        assert result == []

    def test_returns_list(self, temp_dir):
        path = str(temp_dir / "test.txt")
        write_file(path, "test line\n")
        result = search_in_file(path, "test")
        assert isinstance(result, list)
