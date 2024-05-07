# class 정의
class Live:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

# 입력
n = int(input())
# 배열에 저장
listLive = []
for _ in range(n):
    name, addr, city = input().split()
    listLive.append(Live(name, addr, city))

listLive.sort(key=lambda live: live.name)

slowName = listLive[n-1]
print(f"name {slowName.name}")
print(f"addr {slowName.addr}")
print(f"city {slowName.city}")