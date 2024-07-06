offset = 1000
maxSpace = offset * 2
squre = [
    tuple(map(int, input().split()))
    for _ in range(3)
]
check = [
    [0] * (maxSpace+1)
    for _ in range(maxSpace+1)
]
for index, (x1, y1, x2, y2) in enumerate(squre, start=1):
    x1, x2 = offset + x1, offset + x2
    y1, y2 = offset + y1, offset + y2 
    for i in range(x1, x2):
        for j in range(y1, y2):
            check[i][j] = index

cnt = 0
for x in check:
    for y in x:
        if y != index and y != 0:
            cnt += 1
print(cnt)