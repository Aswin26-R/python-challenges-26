import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import generate_secret_number, check_guess, play_round, calculate_score


class TestGenerateSecretNumber:
    def test_within_range(self):
        for _ in range(20):
            result = generate_secret_number(1, 10)
            assert 1 <= result <= 10, f"Expected 1-10, got {result}"

    def test_returns_int(self):
        result = generate_secret_number(1, 100)
        assert isinstance(result, int)

    def test_custom_range(self):
        for _ in range(20):
            result = generate_secret_number(50, 60)
            assert 50 <= result <= 60

    def test_min_equals_max(self):
        result = generate_secret_number(5, 5)
        assert result == 5


class TestCheckGuess:
    def test_too_low(self):
        assert check_guess(7, 5) == "too_low"

    def test_too_high(self):
        assert check_guess(7, 9) == "too_high"

    def test_correct(self):
        assert check_guess(7, 7) == "correct"

    def test_guess_zero_secret_positive(self):
        assert check_guess(10, 0) == "too_low"

    def test_exact_boundary(self):
        assert check_guess(1, 1) == "correct"

    def test_returns_string(self):
        result = check_guess(5, 3)
        assert isinstance(result, str)


class TestPlayRound:
    def test_too_low_round(self):
        result = play_round(7, 5, 3)
        assert result["guess"] == 5
        assert result["result"] == "too_low"
        assert result["attempts"] == 3
        assert result["game_over"] is False

    def test_correct_round(self):
        result = play_round(7, 7, 2)
        assert result["result"] == "correct"
        assert result["game_over"] is True

    def test_too_high_round(self):
        result = play_round(7, 9, 1)
        assert result["result"] == "too_high"
        assert result["game_over"] is False

    def test_returns_dict(self):
        result = play_round(5, 3, 1)
        assert isinstance(result, dict)

    def test_has_all_keys(self):
        result = play_round(5, 3, 1)
        assert "guess" in result
        assert "result" in result
        assert "attempts" in result
        assert "game_over" in result

    def test_game_over_false_when_wrong(self):
        result = play_round(10, 5, 1)
        assert result["game_over"] is False


class TestCalculateScore:
    def test_first_attempt_perfect(self):
        assert calculate_score(1, 10) == 100

    def test_all_attempts_zero(self):
        assert calculate_score(10, 10) == 0

    def test_midpoint(self):
        result = calculate_score(5, 10)
        assert 40 <= result <= 60, f"Expected around 50, got {result}"

    def test_returns_int(self):
        result = calculate_score(3, 10)
        assert isinstance(result, int)

    def test_score_never_negative(self):
        result = calculate_score(10, 10)
        assert result >= 0
