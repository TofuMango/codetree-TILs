n = int(input())

answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

count = 1

# n = 4 일때, 4-1=3, 3,2,1 열만 해당됨.
# 근데 n, 0, -1 하면, 4 3 2 1임. 범위 벗어남. 0 포함 하고 싶으면 -1 써줘야함.
for i in range(n-1, -1, -1):
    if i % 2 == 0:
        for j in range(n):
            answer[j][i] = count
            count += 1
    else:
        for j in range(n-1, -1, -1):
            answer[j][i] = count
            count += 1

for row in answer:
    for col in row:
        print(col, end=' ')
    print()