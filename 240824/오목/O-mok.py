def check_winner(board):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 가로, 세로, 대각선 (↘, ↙)
    
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:  # 바둑알이 놓인 자리
                player = board[i][j]
                for dx, dy in directions:
                    count = 1
                    x, y = i, j
                    
                    # 한 방향 검사
                    while 0 <= x + dx < 19 and 0 <= y + dy < 19 and board[x + dx][y + dy] == player:
                        count += 1
                        x += dx
                        y += dy
                    
                    # 반대 방향 검사
                    x, y = i, j
                    while 0 <= x - dx < 19 and 0 <= y - dy < 19 and board[x - dx][y - dy] == player:
                        count += 1
                        x -= dx
                        y -= dy
                    
                    # 5개가 연속이면 승리
                    if count == 5:
                        # 가운데 위치의 좌표를 계산
                        center_x = i + 2 * dx
                        center_y = j + 2 * dy
                        return player, center_x + 1, center_y + 1  # 1-based index

    return 0, None, None  # 승부 결정되지 않음

# 입력 받기
board = [list(map(int, input().split())) for _ in range(19)]

# 승리 여부 확인
winner, x, y = check_winner(board)

# 결과 출력
print(winner)
if winner != 0:
    print(x, y)

# # 19x19 배열 초기화
# arr = [
#     list(map(int, input().split()))  # 각 줄을 입력받아 정수 리스트로 변환
#     for _ in range(19)
# ]

# # 승리 여부를 확인하기 위한 변수 초기화
# win = 0
# x, y = -1, -1  # 초기값 설정

# # 모든 위치에서 승리 조건 확인
# for i in range(19):
#     for j in range(19):
#         # 검은돌이 이겼는지 확인
#         if arr[i][j] == 1:
#             total1 = total2 = total3 = 0
#             for k in range(5):
#                 if j + k < 19:  # 가로 확인
#                     total1 += arr[i][j + k]
#                 if i + k < 19:  # 세로 확인
#                     total2 += arr[i + k][j]
#                 if i + k < 19 and j + k < 19:  # 대각선 확인
#                     total3 += arr[i + k][j + k]
#             if total1 == 5 or total2 == 5 or total3 == 5:
#                 x, y = i + 1, j + 1  # 인덱스에 1을 더하여 출력
#                 win = 1

#         # 백돌 확인
#         if arr[i][j] == 2:
#             total1 = total2 = total3 = 0
#             for k in range(5):
#                 if j + k < 19:  # 가로 확인
#                     total1 += arr[i][j + k]
#                 if i + k < 19:  # 세로 확인
#                     total2 += arr[i + k][j]
#                 if i + k < 19 and j + k < 19:  # 대각선 확인
#                     total3 += arr[i + k][j + k]
#             if total1 == 10 or total2 == 10 or total3 == 10:  # 백돌은 2로 체크
#                 x, y = i + 1, j + 1  # 인덱스에 1을 더하여 출력
#                 win = 2

# # 결과 출력
# print(win)
# if win != 0:
#     print(x, y)

# # arr = [
# #     list(map(int, input().split()))  # 각 줄을 입력받아 정수 리스트로 변환
# #     for _ in range(19)
# # ]
# # win = 0
# # x = 0
# # y = 0
# # for i in range(0,14,5):
# #     for j in range(0,14,5):
# #         # 검은돌이 이겼는지 확인
# #         if arr[i][j] == 1:
# #             total1 = 0
# #             total2 = 0
# #             total3 = 0
# #             for k in range(5):
# #                 total1 += arr[i][j+k]
# #                 total2 += arr[i+k][j]
# #                 total3 += arr[i+k][j+k]
# #             if total1 == 5 or total2 == 5 or total3 == 5:
# #                 x, y = i, j
# #                 win = 1
# #         # 백돌 확인
# #         if arr[i][j] == 2:
# #             total1 = 0
# #             total2 = 0
# #             total3 = 0
# #             for k in range(5):
# #             # 가로확인
# #                 total1 += arr[i][j+k]
# #                 total2 += arr[i+k][j]
# #                 total3 += arr[i+k][j+k]
# #             if total1 == 5 or total2 == 5 or total3 == 5:
# #                 x, y = i, j
# #                 win = 2
# # print(win)
# # print(x, y)