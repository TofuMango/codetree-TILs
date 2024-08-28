max_ab = 1000000
n = 6
ability = list(map(int, input().split()))
min_diff = max_ab

# 총합차이 구하기
def diff(i, j, k):
    sum1 = ability[i] + ability[j] + ability[k]
    sum2 = sum(ability) - sum1
    return abs(sum1 - sum2)

# 3개의 인덱스를 선택하여 최소 차이 계산
for i in range(n):
    # i보다 큰 인덱스 선택
    for j in range(i + 1, n):
        # j보다 큰 인덱스 선텍
        for k in range(j + 1, n):
            min_diff = min(min_diff, diff(i, j, k))

print(min_diff)