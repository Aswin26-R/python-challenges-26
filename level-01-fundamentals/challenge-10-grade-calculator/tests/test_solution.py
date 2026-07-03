import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import calculate_average, get_letter_grade, create_report

class TestCalculateAverage:
    def test_basic_average(self):
        assert calculate_average([90, 85, 92, 88]) == 88.75

    def test_two_scores(self):
        assert calculate_average([100, 0]) == 50.0

    def test_single_score(self):
        assert calculate_average([100]) == 100.0

    def test_empty_list(self):
        assert calculate_average([]) == 0.0

    def test_rounds_to_two_decimals(self):
        result = calculate_average([55, 60, 45])
        assert result == 53.33

    def test_returns_float(self):
        result = calculate_average([90, 80])
        assert isinstance(result, float)


class TestGetLetterGrade:
    def test_a_grade_high(self):
        assert get_letter_grade(100) == "A"

    def test_a_grade_low(self):
        assert get_letter_grade(90) == "A"

    def test_b_grade_high(self):
        assert get_letter_grade(89) == "B"

    def test_b_grade_low(self):
        assert get_letter_grade(80) == "B"

    def test_c_grade_high(self):
        assert get_letter_grade(79) == "C"

    def test_c_grade_low(self):
        assert get_letter_grade(70) == "C"

    def test_d_grade_high(self):
        assert get_letter_grade(69) == "D"

    def test_d_grade_low(self):
        assert get_letter_grade(60) == "D"

    def test_f_grade_high(self):
        assert get_letter_grade(59) == "F"

    def test_f_grade_zero(self):
        assert get_letter_grade(0) == "F"

    def test_returns_string(self):
        result = get_letter_grade(85)
        assert isinstance(result, str)


class TestCreateReport:
    def test_basic_report(self):
        report = create_report("Alice", [90, 85, 92])
        assert report["name"] == "Alice"
        assert report["scores"] == [90, 85, 92]
        assert report["average"] == 89.0
        assert report["grade"] == "B"

    def test_report_is_dict(self):
        result = create_report("Bob", [70, 75, 80])
        assert isinstance(result, dict)

    def test_report_has_all_keys(self):
        result = create_report("Test", [80])
        assert "name" in result
        assert "scores" in result
        assert "average" in result
        assert "grade" in result

    def test_f_grade_report(self):
        report = create_report("Charlie", [55, 60, 45])
        assert report["name"] == "Charlie"
        assert report["average"] == 53.33
        assert report["grade"] == "F"

    def test_a_grade_report(self):
        report = create_report("Diana", [95, 92, 98])
        assert report["grade"] == "A"

    def test_scores_preserved(self):
        scores = [80, 90, 70]
        report = create_report("Eve", scores)
        assert report["scores"] == [80, 90, 70]
