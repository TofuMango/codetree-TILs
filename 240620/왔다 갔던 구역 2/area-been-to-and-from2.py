offerset = 1000
max_space = 2000
n = int(input())
segments = [tuple(input().split()) for _ in range(n)]
res = [0] * (max_space + 1)

for x, y in segments:
    x = int(x)
    if y == 'R':
        for i in range(x):
            res[offerset + i] += 1
        offerset += x  # 한 번에 x만큼 증가

    elif y == 'L':
        for i in range(x):
            res[offerset - i] += 1
        offerset -= x  # 한 번에 x만큼 감소

cnt = 0
for r in res:
    if r >= 2:
        cnt += 1

print(cnt)