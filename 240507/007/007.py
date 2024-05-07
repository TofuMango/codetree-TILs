# class Student:
#     def __init__(self, kor, eng, math):
#         # self는 student 를 지칭...
#         self.kor = kor
#         self.eng = eng
#         self.math = math

# student1 = Student(90, 80, 90)
# print(student1.kor)  # 90
# print(student1.eng)  # 80
# print(student1.math) # 90


class secretcode:
    def __init__(self, code, meet, time):
        self.code = code
        self.meet = meet
        self.time = time

cd, mt, t = input().split()
secretC = secretcode(cd, mt, t)
print("secret code :", secretC.code)
print("meeting point :", secretC.meet)
print("time :", secretC.time)