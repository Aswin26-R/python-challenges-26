import random


def generate_secret_number(min_val, max_val):
    """
    TODO:
    Return a random integer between min_val and max_val (both inclusive).

    Examples:
        generate_secret_number(1, 10)   → some integer from 1 to 10
        generate_secret_number(50, 100) → some integer from 50 to 100

    Hint: Use random.randint(min_val, max_val)
          randint is "inclusive" — both min and max can be returned.
    """
    pass


def check_guess(secret, guess):
    """
    TODO:
    Compare the guess to the secret number and return a result string.

    Return values:
        "too_low"  — if guess is less than secret
        "too_high" — if guess is greater than secret
        "correct"  — if guess equals secret

    Examples:
        check_guess(7, 5)  → "too_low"
        check_guess(7, 9)  → "too_high"
        check_guess(7, 7)  → "correct"

    Hint: Use if/elif/else comparing guess to secret.
    """
    pass


def play_round(secret, guess, attempts):
    """
    TODO:
    Process one round of the guessing game and return a result dictionary.

    Parameters:
        secret   — the secret number
        guess    — the player's guess
        attempts — how many attempts the player has used (including this one)

    Return a dictionary with:
        "guess"     — the player's guess
        "result"    — "too_low", "too_high", or "correct"
        "attempts"  — the number of attempts used
        "game_over" — True if the guess is correct, False otherwise

    Examples:
        play_round(7, 5, 3)  → {"guess": 5, "result": "too_low",  "attempts": 3, "game_over": False}
        play_round(7, 7, 2)  → {"guess": 7, "result": "correct",  "attempts": 2, "game_over": True}
        play_round(7, 9, 1)  → {"guess": 9, "result": "too_high", "attempts": 1, "game_over": False}

    Hint: Use check_guess(secret, guess) to get the result, then build the dict.
    """
    pass


def calculate_score(attempts, max_attempts):
    """
    TODO:
    Calculate a score from 0 to 100 based on how many attempts were used.

    Rules:
        - 1 attempt → 100 points (perfect score)
        - max_attempts → 0 points (used all guesses)
        - Linear scale in between

    Examples:
        calculate_score(1, 10)   → 100
        calculate_score(10, 10)  → 0
        calculate_score(5, 10)   → 50 (approximately)

    Hint: One formula that works:
          remaining = max_attempts - attempts
          score = int(100 * remaining / (max_attempts - 1))
          return max(0, score)

    You can use any formula that gives 100 for attempts=1 and 0 for attempts=max_attempts.
    """
    pass
