from util import avg

n = int(input("Enter the total no. of students: "))
student_marks = {}

for i in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input("Enter the name of student to calculate his/her average score: ")
average = avg(student_marks, query_name)
print(round(average, 2))