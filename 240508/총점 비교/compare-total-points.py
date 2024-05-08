class Student:
    def __init__(self, name, s1, s2, s3):
        self.name, self.s1, self.s2, self.s3 = name, s1, s2, s3
n = int(input())
students = []
for _ in range(n):
    name, sub1, sub2, sub3 = input().split()
    students.append(Student(name, int(sub1), int(sub2), int(sub3)))
students.sort(key=lambda x: x.s1 + x.s2 + x.s3)
for student in students:
    print(student.name, student.s1, student.s2, student.s3)