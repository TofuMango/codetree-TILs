# 입력
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
# 최대합 찾는 로직
# n이 6, k가 3이라 하면 n에다 k 빼서 0,1,2까지만 돌도록
for i in range(n-k):
    hap = 0
    for j in range(i, i+k):
        hap += arr[j]
    ans = max(ans, hap)
print(ans)