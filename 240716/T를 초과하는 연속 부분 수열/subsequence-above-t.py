# n, t = map(int, input().split())
# arr = list(map(int, input().split()))

# ans, cnt = 0, 0

# for i in range(n):
#     if arr[i] > t:
#         cnt += 1
#     else:
#         cnt = 0
#     ans = max(ans, cnt)

# print(ans)
n,t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
ans, cnt = 0,0
for i in range(n):
    if i >= 1 and (arr[i] > t and arr[i] > arr[i-1]):
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)
print(ans)