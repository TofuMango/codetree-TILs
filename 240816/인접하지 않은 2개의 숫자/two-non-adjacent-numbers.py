import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# 인접하지 않은 모든 쌍 잡기
ans = INT_MIN
for i in range(n):
    for j in range(i + 2, n):
        # 현재 ans가 두숫자 합보다 작다면 ans 다시 업데이트
        if ans < arr[i] + arr[j]:
            ans = arr[i] + arr[j]

print(ans)
# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     hap = 0
#     for j in range(n):
#         # 0 0 아니면서
#         # 2일땐 1이어야하는데 ...바로 옆에 붙지않으면서.
#         if i == j or abs(i-j) == 1:
#             continue
#         else:
#             hap = arr[i] + arr[j]
#             ans = max(ans, hap)
        
# print(ans)