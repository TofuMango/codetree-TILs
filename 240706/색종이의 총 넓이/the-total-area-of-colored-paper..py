offset = 100
maxSpace = offset * 2
n = int(input())
paper = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
check = [
    [0] * (maxSpace+1)
    for _ in range(maxSpace+1)
]

for x, y in paper:
    for i in range(x, x+8):
        for j in range(y, y+8):
            check[i][j] = 1
cnt = 0
for i in range(0, maxSpace+1):
    for j in range(0, maxSpace+1):
        if check[i][j] == 1:
            cnt += 1
print(cnt)