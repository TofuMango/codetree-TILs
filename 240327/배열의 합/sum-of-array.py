# n = 4
# for a in range(n):
#     arr = list(map(int, input().split()))
#     sum_val = sum(arr)
#     print(sum_val)

# 2차원 배열 사용, 각줄마다 정수 입력받음
arr_2d = [
    list(map(int, input().split()))
    for a in range(4)
]

for i in range(4):
    print(sum(arr_2d[i]))