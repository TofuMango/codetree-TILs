# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
# 구간시작점
for i in range(n): 
    # 구간 끝점
    for j in range(i, n): 
        # 구간 [i, j] 내 원소의 합
        sum_interval = 0
        for k in range(i, j + 1):
            sum_interval += arr[k]
        # 평균구하기(합계/끝-처음 + 1)
        avg = sum_interval / (j - i + 1)

        exists = False
        for k in range(i, j + 1):
            # 만약 구간내 원소랑 평균이랑 같다면 true
            if arr[k] == avg:
                exists = True
        # true인 경우만 cnt +1
        if exists:
            cnt += 1
                        
print(cnt)