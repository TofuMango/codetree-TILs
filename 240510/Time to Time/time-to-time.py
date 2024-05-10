hour, mins, end_hour, min_hour = tuple(map(int, input().split()))
elapsed_time = 0
while True:
    if hour == end_hour and mins == min_hour:
        break
    # 분단위임
    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(elapsed_time)