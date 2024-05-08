class Subject:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, int(kor), int(eng), int(math)

# 입력
n= int(input())
# 정보 저장할 배열 선언
students = []
# 배열에 정보 저장
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append(Subject(name, kor, eng, math))
# 정렬(내림차순)
students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))
# 출력
for student in students:
    print(student.name, student.kor, student.eng, student.math)