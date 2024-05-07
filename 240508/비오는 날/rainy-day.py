class Inform:
    def __init__(self, year, day, weather):
        self.year = year
        self.day = day
        self.weather = weather

# 입력
n = int(input())
# 배열에 정보 저장
arr = [
    tuple(input().split())
    for _ in range(n)
]

info = [
    Inform(year, day, weather) 
    for year, day, weather in arr
]

minIndex = 0
for i, data in enumerate(info):
    if data.weather == "Rain":
        if data.year < info[minIndex].year:
            minIndex = i
            
print(f"{info[minIndex].year} {info[minIndex].day} {info[minIndex].weather}")