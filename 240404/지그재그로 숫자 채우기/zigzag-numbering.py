# 내가 푼 풀이
n, m = tuple(map(int, input().split()))

arr_1 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

sum = 0
# 열
for i in range(m):
    # 행
    for j in range(n):
        # 열이 짝수 일때(0,2,4 ...)
        if i % 2 == 0 :
            arr_1[j][i] = sum
            sum += 1
        else:
            arr_1[n-1-j][i] = sum
            sum += 1

for row in arr_1:
    for col in row:
        print(col, end=' ')
    print()

# 해설
# 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# answer = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# count = 0

# # Step 1:
# for col in range(m):
#     if col % 2 == 0:
#         # Case 1:
#         for row in range(n):
#             answer[row][col] = count
#             count += 1
#     else:
#         # Case 2:
#         for row in range(n - 1, -1, -1):
#             answer[row][col] = count
#             count += 1

# # 출력:
# for row in range(n):
#     for col in range(m):
#         print(answer[row][col], end = ' ')
#     print()