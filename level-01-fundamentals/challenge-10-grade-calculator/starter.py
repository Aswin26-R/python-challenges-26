class grade_calculator:
    def calculate_average(scores):
        if not scores:
            return 0.0
        average = sum(scores) / len(scores)
        return round(average,2)
        pass

    def get_letter_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
        pass
    


    def create_report(student_name, scores):
        average = grade_calculator.calculate_average(scores)
        grade = grade_calculator.get_letter_grade(average)
        return({
            "name":student_name,
            "scores":scores,
            "average":average,
            "grade":grade})
    pass


print(grade_calculator.calculate_average([100,0]))
print(grade_calculator.get_letter_grade(59))
print(grade_calculator.create_report("Aswin", [69, 70, 75,88,95]))
