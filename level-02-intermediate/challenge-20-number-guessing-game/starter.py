import random


def generate_secret_number(min_val, max_val):
    return random.randint(min_val,max_val)
    pass
print(generate_secret_number(50, 100))

def check_guess(secret, guess):
    if secret > guess:
        return "too_low"
    elif secret < guess:
        return "too_high"
    else:
        return "correct"
    pass
print(check_guess(7,7))

def play_round(secret, guess, attempts):
    result = check_guess(secret,guess)
    return {
        "guess" : guess,
        "result": result,
        "attempts": attempts,
        "game_over": result == "correct"
        }
    pass
print(play_round(7,7,2))

def calculate_score(attempts, max_attempts):
    remaining = max_attempts - attempts
    score = int(100 * remaining/(max_attempts - 1))
    return max(0,score)
    pass
print(calculate_score(10,10))