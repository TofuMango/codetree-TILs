# 변수 선언 및 입력
n = int(input())


# Forecast 정보를 나타내는 클래스 선언
class Forecast:
    def __init__(self, date, day, weather):
        self.date, self.day, self.weather = date, day, weather


ans = Forecast("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = tuple(input().split())
    # Forecast 객체를 만들어 줍니다.
    f = Forecast(date, day, weather)
    if weather == "Rain":
        # 비가 오는 경우 가장 최근인지 확인하고,
        # 가장 최근일 경우 정답을 업데이트합니다.
        if ans.date >= f.date:
            ans = f

# 결과를 출력합니다.
print(ans.date, ans.day, ans.weather)

# class Inform:
#     def __init__(self, date, day, weather):
#         self.date = date
#         self.day = day
#         self.weather = weather

# # 입력 받기
# n = int(input())

# # Inform 객체들을 저장할 리스트 생성
# info_list = []

# for _ in range(n):
#     date, day, weather = input().split()
#     info = Inform(date, day, weather)
#     info_list.append(info)

# # 비가 오는 날 중 가장 빠른 날짜를 찾기 위한 변수 초기화
# earliest_rain = None

# # 비가 오는 날 중 가장 빠른 날짜 찾기
# for info in info_list:
#     if info.weather == "Rain":
#         if earliest_rain is None or info.date < earliest_rain.date:
#             earliest_rain = info

# # 결과 출력
# print(f"{earliest_rain.date} {earliest_rain.day} {earliest_rain.weather}")

# class Inform:
#     def __init__(self, year, day, weather):
#         self.year = year
#         self.day = day
#         self.weather = weather

# # 입력
# n = int(input())
# # 배열에 정보 저장
# arr = [
#     tuple(input().split())
#     for _ in range(n)
# ]

# info = [
#     Inform(year, day, weather) 
#     for year, day, weather in arr
# ]

# # 비가 오는 날 중 가장 빠른 날짜를 찾기 위한 변수 초기화
# earliest_rain = None

# # 비가 오는 날 중 가장 빠른 날짜 찾기
# for i in info:
#     if i.weather == "Rain":
#         if earliest_rain is None or i.date < earliest_rain.date:
#             earliest_rain = i

# print(f"{earliest_rain.date} {earliest_rain.day} {earliest_rain.weather}")