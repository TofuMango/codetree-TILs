# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]
count = 1
        
# 시작열(case1)
for start_col in range(m):
    # 현재 행
    curr_row = 0
    # 현재 열 = 시작점
    curr_col = start_col

    # 현재 열이 0보다 크거나 같고, 현재 행이 n보다 작을때
    # 이때, 열이 0보다 작아지면 범위를 벗어나게됨. 다만, 범위를 넘어가는(m)일은 열을 계속 감소시키기 때문에 일어나지 않음. 
    while 0 <= curr_col and curr_row < n:
        # arr[현재행][현재열] = count변수
        answer[curr_row][curr_col] = count
        
        # 변수 업데이트
        # 행은 늘어남
        curr_row += 1
        # 열은 감소함
        curr_col -= 1
        count += 1

# 시작행(1부터 n 바로 앞까지), 이미 0행은 처리했기 때문.
for start_row in range(1, n):
    # 현재행 = 시작행(1행부터 시작)
    curr_row = start_row
    # 현재 열 = 열-1(3x3 배열일때, 1행 2열부터 시작)
    curr_col = m - 1
    # 현재 열이 0보다 크거나 같고, 현재 행이 n보다 작을때(범위 내일때)
    while 0 <= curr_col and curr_row < n:
        # arr[행][열]
        answer[curr_row][curr_col] = count
        
        # 변수 업데이트
        # 2번째 while은 2행 1열이 됨.
        # 3번째 while은 3행이 되므로 while 조건문 빠져나옴.
        # 그럼 현재행은 2행이 되고, 2행 2열 부터 다시채움.
        # while 2번째는 3행 1열이 되기때문에 범위 벗어남. for 반복문 종료.
        curr_row += 1
        curr_col -= 1
        count += 1

# 출력:
# for row in range(n):
#     for col in range(m):
#         print(answer[row][col], end = ' ')
#     print()

for row in answer:
    for col in row:
        print(col, end=' ')
    print()