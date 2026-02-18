from collections import namedtuple
def marks(n, columns, rows):
    Student = namedtuple('Student', columns)
    total = 0
    for row in rows:
        student = Student(*row.split())
    total += int(student.MARKS)
    average= total/n

    return(average)