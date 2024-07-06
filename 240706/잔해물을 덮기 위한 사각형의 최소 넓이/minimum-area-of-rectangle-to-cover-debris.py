offset = 1000
maxSpace = offset * 2
square = [
    tuple(map(int, input().split()))
    for _ in range(2)
]
check = [
    [0] * (maxSpace+1)
    for _ in range(maxSpace+1)
]
for index, (x1, y1, x2, y2) in enumerate(square, start = 1):
    x1, y1 = offset+x1, offset+y1
    x2, y2 = offset+x2, offset+y2
    for i in range(x1, x2):
        for j in range(y1, y2):
            check[i][j] = index

x_max = 0
y_max = 0

# x_max 계산
for i in range(0, maxSpace+1):
    tmp = 0
    for j in range(0, maxSpace+1):
        if check[i][j] == 1:
            tmp += 1
        else:
            if x_max < tmp:
                x_max = tmp
            tmp = 0
    if x_max < tmp:
        x_max = tmp

# y_max 계산
for j in range(0, maxSpace+1):
    tmp = 0
    for i in range(0, maxSpace+1):
        if check[i][j] == 1:
            tmp += 1
        else:
            if y_max < tmp:
                y_max = tmp
            tmp = 0
    if y_max < tmp:
        y_max = tmp

print(x_max * y_max)