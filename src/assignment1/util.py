def avg(student_marks, query_name):
    marks_list = student_marks[query_name]
    avg = sum(marks_list) / len(marks_list)
    return avg 