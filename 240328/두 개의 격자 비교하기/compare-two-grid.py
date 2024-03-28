n, m = tuple(map(int, input().split()))

arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_3 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        # 같으면 0, 그렇지 않다면 1
        if arr_1[i][j] != arr_2[i][j]:
            arr_3[i][j] = 1

for row in arr_3:
    for result in row:
        print(result, end=" ")
    print()