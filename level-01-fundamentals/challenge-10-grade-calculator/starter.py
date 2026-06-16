def calculate_average(scores):
    """
    TODO:
    Return the average of the list of scores, rounded to 2 decimal places.
    If the list is empty, return 0.0.

    Examples:
        calculate_average([90, 85, 92, 88])  should return 88.75
        calculate_average([100, 0])           should return 50.0
        calculate_average([100])              should return 100.0
        calculate_average([])                 should return 0.0

    Hint:
        average = sum(scores) / len(scores)
        return round(average, 2)

        Don't forget to handle the empty list case first!
    """
    pass


def get_letter_grade(score):
    """
    TODO:
    Return the letter grade for the given numeric score.

    Grading scale:
        90 - 100  →  "A"
        80 - 89   →  "B"
        70 - 79   →  "C"
        60 - 69   →  "D"
        0  - 59   →  "F"

    Examples:
        get_letter_grade(95)   should return "A"
        get_letter_grade(90)   should return "A"
        get_letter_grade(85)   should return "B"
        get_letter_grade(72)   should return "C"
        get_letter_grade(65)   should return "D"
        get_letter_grade(45)   should return "F"
        get_letter_grade(0)    should return "F"

    Hint: Use if/elif/else, starting from the highest score:
        if score >= 90:
            return "A"
        elif score >= 80:
            ...
    """
    pass


def create_report(student_name, scores):
    """
    TODO:
    Return a dictionary containing the student's name, scores, average, and grade.

    The dictionary should have exactly these keys:
        "name"    — the student's name (string)
        "scores"  — the list of scores (list)
        "average" — the calculated average (float, rounded to 2 decimal places)
        "grade"   — the letter grade (string)

    Examples:
        create_report("Alice", [90, 85, 92])
        should return:
        {
            "name": "Alice",
            "scores": [90, 85, 92],
            "average": 89.0,
            "grade": "B"
        }

        create_report("Bob", [55, 60, 45])
        should return:
        {
            "name": "Bob",
            "scores": [55, 60, 45],
            "average": 53.33,
            "grade": "F"
        }

    Hint: Use your calculate_average() and get_letter_grade() functions inside this one.
          Build and return a dictionary: {"name": student_name, "scores": scores, ...}
    """
    pass
