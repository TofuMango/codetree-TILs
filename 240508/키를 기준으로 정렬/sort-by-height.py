# class 정의
class Student:
    def __init__(self, name, height, weight):
         self.name, self.height, self.weight = name, int(height), int(weight)
# 입력
n = int(input())
# 학생 데이터 입력받기
students = [] # 학생 객체를 저장할 리스트를 생성
for _ in range(n):
    name, height, weight = tuple(input().split())
    # student = Student(name, height, weight) # Student 객체를 생성하고 변수에 할당
    # students.append(student) # 생성된 객체를 students 리스트에 추가
    students.append(Student(name, int(height), int(weight)))
# 키 기준으로 정렬
students.sort(key=lambda x : x.height)

for student in students:
    print(student.name, student.height, student.weight)