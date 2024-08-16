n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    hap = 0
    for j in range(n):
        # 0 0 아니면서
        # 2일땐 1이어야하는데 ...바로 옆에 붙지않으면서.
        if i == j or abs(i-j) == 1:
            continue
        else:
            hap = arr[i] + arr[j]
            ans = max(ans, hap)
        
print(ans)