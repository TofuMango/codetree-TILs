# class 정의
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight
# 자료 수 입력받기
n= int(input())
# 객체 생성
students = []
# 배열에 저장
for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append((Student(name, int(height), int(weight))))

# 정렬
students.sort(key=lambda x: (x.height, -x.weight))

# 출력
for student in students:
    print(student.name, student.height, student.weight)