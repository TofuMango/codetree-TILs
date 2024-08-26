import sys
n, h, t = map(int, input().split())
arr = list(map(int, input().split()))
min_ex = sys.maxsize

for i in range(n-t+1):
    exp = 0
    for j in range(i, i+t):
        # 현재 높이가 주어진 높이보다 작을때
        if arr[j] < h:
            exp += h - arr[j]
        # 현재 높이가 주어진 높이보다 클때
        elif arr[j] > h:
            exp += arr[j] - h
        # abs써서 한문장으로 줄이기
        # cost += abs(arr[j] - h)
        
    min_ex = min(min_ex, exp)
print(min_ex)