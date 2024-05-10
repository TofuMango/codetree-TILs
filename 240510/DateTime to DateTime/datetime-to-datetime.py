# 시간차 많이 안날때
day, hour, miniute = 11, 11, 11
a, b, c = tuple(map(int, input().split()))
elapsed_time = 0

while True:
    if a < day and b < hour and c < miniute:
        print(-1)
        break 
    if day == a and hour == b and miniute == c:
        print(elapsed_time)
        break
    
    elapsed_time += 1
    miniute += 1

    if miniute >= 60:
        hour += 1
        miniute = 0

    if hour >= 24:
        day += 1
        hour = 0
        miniute = 0
# 많이 날때
# # 변수 선언 및 입력
# a, b, c = tuple(map(int, input().split()))

# # 차이를 계산.
# diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

# # 출력
# if diff < 0:
#     print(-1)
# else:
#     print(diff)