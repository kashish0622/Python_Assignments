def avg(student_marks, query_name):
    avg_marks = 0
    marks_list = student_marks[query_name]
    avg_marks = sum(marks_list) / len(marks_list)
    return avg_marks