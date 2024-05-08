class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight
n = 5
students1 = []
students2 = []
for i in range(n):
    name, height, weight = tuple(input().split())
    students1.append(Student(name, int(height), float(weight)))
    students2.append(Student(name, int(height), float(weight)))

students1.sort(key=lambda x: x.name)
students2.sort(key=lambda x: -x.height)

print("name")
for student in students1:
    print(student.name, student.height, format(student.weight,".1f"))
print()

print("height")
for student in students2:
    print(student.name, student.height, format(student.weight,".1f"))