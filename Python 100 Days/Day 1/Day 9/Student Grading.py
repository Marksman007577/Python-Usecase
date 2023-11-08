import pandas as pd

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Droco": 74,
    "Neville": 62,
}

converted_grade = {}

for key in student_scores:
    if student_scores[key] >= 91:
        converted_grade[key] = "Outstanding"
    elif (student_scores[key] >= 81) and (student_scores[key] <= 90):
        converted_grade[key] = "Excellent"
    elif (student_scores[key] >= 71) and (student_scores[key] <= 80):
        converted_grade[key] = "Acceptable"
    else:
        converted_grade[key] = "Fail"

formatted_converted_grade = pd.DataFrame.from_dict(converted_grade, orient='index')
print(formatted_converted_grade)
