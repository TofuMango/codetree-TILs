n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

ans, cnt = 0, 0
for i in range(n):
    # i가 음수이거나, 음수이면서 연속하는 원소가 동일한 음수인 경우 +1
    if arr[i] < 0 or (arr[i] < 0 and arr[i] == arr[i-1]):
        cnt += 1
    # 그렇지 않으면 cnt를 1로 초기화
    else:
        cnt = 1
    ans = max(ans, cnt)
print(ans-1)