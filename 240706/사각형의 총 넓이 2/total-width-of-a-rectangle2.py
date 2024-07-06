offset = 100
maxSpace = 200
cur = maxSpace
n = int(input())
# x,y축이 최대 100인 2차원 평면 생성
arr = [[0 for _ in range(maxSpace)] for _ in range(maxSpace)]
for square in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

cnt = 0
for x in arr:
    for y in x:
        if y == 1:
            cnt +=1
print(cnt)