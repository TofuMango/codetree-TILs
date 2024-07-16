n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

ans, cnt = 1, 1  # 첫 번째 숫자는 항상 포함되므로 1로 초기화
for i in range(1, n):  # 두 번째 숫자부터 시작
    if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0):  # 부호가 동일한지 확인
        cnt += 1
    else:
        cnt = 1  # 부호가 다르면 cnt를 1로 초기화
    ans = max(ans, cnt)  # 최대 길이를 갱신

print(ans)