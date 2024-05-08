class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num  # 입력받은 순서대로 번호 부여

# 입력
n = int(input())
students = []
for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i+1))  # i+1로 번호 부여

# 정렬하기
# 키가 더 큰 학생이 앞에 오도록, 그 다음 몸무게가 더 큰 학생이 앞에 오도록, 그리고 입력 순서(번호)가 작은 학생이 앞에 오도록 정렬
students.sort(key=lambda x: (-x.h, -x.w, x.num))

# 출력하기
for student in students:
    print(student.h, student.w, student.num)