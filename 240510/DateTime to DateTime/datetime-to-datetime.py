day, hour, miniute = 11, 11, 11
a, b, c = tuple(map(int, input().split()))
elapsed_time = 0

while True:
    if a < day and b < hour and c < miniute:
        print(-1)
        break 
    if day == a and hour == b and miniute == c:
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

if elapsed_time != 0:
    print(elapsed_time)