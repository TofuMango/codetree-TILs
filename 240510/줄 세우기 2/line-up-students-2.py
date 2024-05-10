class Student:
    def __init__(self, height, weight, index):
        self.height, self.weight, self.index = height, weight, index
n = int(input())

students = []
for i in range(n):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, i+1))
students.sort(key=lambda x: (x.height, -x.weight))
# 출력
for student in students:
    print(student.height, student.weight, student.index)