# 기본개념 문제
# n = 3
# answer = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]

# count = 1
# for row in range(n):
#     for col in range(n):
#         answer[row][col] = count
#     count += 2

# for row in answer:
#     for col in row:
#         print(col, end=' ')
#     print()

# 배열로 사각형 만들기
n = 5
answer =[
    [0 for _ in range(n)]
    for _ in range(n)
]

# for row in range(n):
#     answer[0][row] = 1
# for col in range(n):
#     answer[col][0] = 1

for i in range(n):
    answer[0][i] = 1
    answer[i][0] = 1

for row in range(1,n):
    for col in range(1,n):
        answer[row][col] = answer[row][col-1] + answer[row-1][col]
    
for row in answer:
    for col in row:
        print(col, end=" ")
    print()