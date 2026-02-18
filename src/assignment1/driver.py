from util import avg

n = int(input())
student_marks = {}

for i in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input()
average = avg(student_marks, query_name)
print(round(average, 2))