month, day, end_month, end_day = tuple(map(int, input().split()))
elapsed_day = 0
# 윤년X 기준 2월은 28일까지
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == end_month and day == end_day:
        break
    elapsed_day += 1
    day += 1

    if day> num_of_days[month]:
        month+=1
        day = 1
print(elapsed_day)