# # n과 m 입력 받기
# n, m = tuple(map(int, input().split()))

# # 동전 위치 입력 받기
# place = [
#     list(map(int, input().split())) 
#     for _ in range(m)]

# # 격자 상태 초기화
# answer = [
#     [0 for _ in range(n)] 
#     for _ in range(n)]

# # 동전 위치에 따라 격자 상태 업데이트
# for r, c in place:
#     answer[r-1][c-1] = 1  # 격자와 입력 좌표의 인덱스 차이 조정

# # 격자 상태 출력
# for row in answer:
#     for col in row:
#         print(col, end=' ')
#     print()

# 해설
# 격자 크기 n, 입력받는 동전갯수 m 
n, m = tuple(map(int, input().split()))

# 2차원 배열 구현
answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# m회에 걸쳐 동전 위치 입력받고 1 표기
for _ in range(m):
    r, c = map(int, input().split())
    answer[r-1][c-1] = 1

# 배열 출력(0이 아닌 1부터 시작이니까...)
for row in range(n):
    for col in range(n):
        print(answer[row][col], end = " ")
    print()