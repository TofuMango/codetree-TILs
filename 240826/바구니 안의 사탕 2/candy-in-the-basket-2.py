max_len = 100
n, k = map(int, input().split())
arr = [0] * (max_len+1)
for _ in range(n):
    candy, basket = map(int, input().split())
    # 같은 위치에 여러 바구니가 놓일수잇음
    arr[basket] += candy
# 모든구간 시작점 잡기
max_sum = 0
for i in range(max_len):
    # 구간 내 원소 합 구하기
    sum_all = 0
    for j in range(i-k, i+k+1):
        # 구간의 범위를 벗어나지 않으면
        if j >= 0 and j <= max_len:
            sum_all += arr[j]
    # 최대값 구하기
    max_sum = max(max_sum, sum_all)
print(max_sum)