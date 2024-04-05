n = int(input())

answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

count = 1

# 오른쪽 아래에서 시작
for i in range(n-1, -1, -1):
    # 5-1-4 = 0 %2 == 0임
    # 근데 만약 i%2 == 0 으로 했다면 3 % 2 = 0이 아님. 그래서 else가 됐음
    # 4-1-3 = 0 % 2 == 0 이지..뭔짓을 해도 시작은 아래에서 위로 채울 수 밖에 없음.
    if (n-1-i) % 2 == 0:
        # 열의 인덱스가 짝수일 때 아래에서 위로 채우기
        for j in range(n-1, -1, -1):
            answer[j][i] = count
            count += 1
    else:
        # 열의 인덱스가 홀수일 때 위에서 아래로 채우기
        for j in range(n):
            answer[j][i] = count
            count += 1

# 결과 출력
for row in answer:
    for col in row:
        print(col, end=' ')
    print()