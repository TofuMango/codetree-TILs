# 비교를 위해 큰값부터
import sys
INT_MAX = sys.maxsize
# 입력
n = int(input())
# 가구별 사람 수 입력
info = tuple(map(int, input().split()))
min_dist = INT_MAX
# 이동거리합 구하기
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j-i) * info[j]
    min_dist = min(min_dist, sum_dist)
print(min_dist)