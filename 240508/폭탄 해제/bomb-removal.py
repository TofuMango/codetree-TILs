# class
class solution:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec
# 입력
code, color, sec = input().split()
# 객체생성
clear = solution(code, color, sec)
# 출력
print(f"code : {clear.code}")
print(f"color : {clear.color}")
print(f"second : {clear.sec}")