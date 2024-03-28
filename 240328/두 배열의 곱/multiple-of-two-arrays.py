arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
# 줄 간격
empty = input()

arr_2d_2=[
    list(map(int, input().split()))
        for _ in range(3)
]
result = 0

for i in range(3):
    for j in range(3):
        result = (arr_2d_1[i][j]) * (arr_2d_2[i][j])
        print(result, end=" ")
    print()