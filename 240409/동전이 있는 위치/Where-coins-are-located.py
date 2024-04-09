# n과 m 입력 받기
n, m = map(int, input().split())

# 동전 위치 입력 받기
place = [
    list(map(int, input().split())) 
    for _ in range(m)]

# 격자 상태 초기화
answer = [
    [0 for _ in range(n)] 
    for _ in range(n)]

# 동전 위치에 따라 격자 상태 업데이트
for r, c in place:
    answer[r-1][c-1] = 1  # 격자와 입력 좌표의 인덱스 차이 조정

# 격자 상태 출력
for row in answer:
    for col in row:
        print(col, end=' ')
    print()