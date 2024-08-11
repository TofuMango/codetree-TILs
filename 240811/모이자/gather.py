# 비교를 위해 큰값부터
import sys
INT_MIN = sys.maxsize
# 입력
n = int(input())
# 가구별 사람 수 입력
info = tuple(map(int, input().split()))
# 이동거리합 구하기
for i in range(n):
    sum_diff = 0
    for j in range(n):
        # 0+1-0 = 1, 1+1-0= 2 
        # 0+1-1 = 0, 1+1-1=1
        # 1+1-0  = 2 1+1-1 = 1 
        sum_diff += abs((j-i) * info[j])
    INT_MIN = min(sum_diff, INT_MIN)
print(INT_MIN)