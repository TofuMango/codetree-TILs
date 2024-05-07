# 클래스 선언
class secretcode:
    def __init__(self, code, meet, time):
        self.code = code
        self.meet = meet
        self.time = time

# 변수 선언 
cd, mt, t = input().split()

# 객체 생성
secretC = secretcode(cd, mt, t)

# 출력
print("secret code :", secretC.code)
print("meeting point :", secretC.meet)
print("time :", secretC.time)