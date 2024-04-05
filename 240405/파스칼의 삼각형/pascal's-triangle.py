n = int(input())
answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    answer[i][0] = 1

for row in range(1, n):
    for col in range(1, n):
        answer[row][col] = answer[row-1][col-1] + answer[row-1][col]

for row in answer:
    for col in row:
        if col != 0:
            print(col, end=' ')
    print()

# # 2차원 배열을 구현합니다.
# arr = [
#     [0 for _ in range(15)]
#     for _ in range(15)
# ]
	
# # n을 입력받습니다.
# n = int(input())
	
# # 배열의 각 행의 첫 열과 마지막 열을 1로 초기화합니다.
# for i in range(n):
# 	arr[i][0] = 1
# 	arr[i][i] = 1
	
# # 배열의 숫자를 채웁니다.
# for i in range(n):
#     # 1부터 0까지, 1부터 1까지, 1부터 2까지 1부터 3까지...
#     # (0,0)(1,0)(2,)
# 	for j in range(1, i):
# 		arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

# # 채워진 배열을 출력합니다.
# # 행은 n이 6일때 0,1,2,3,4,5 까지.
# for i in range(n):
#     # 열은 (0,1)(0,2)(0,3)(0,4)(0,5)
# 	for j in range(i + 1):
# 		print(arr[i][j], end=" ")
# 	print()