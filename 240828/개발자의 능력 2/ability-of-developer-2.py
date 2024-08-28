max_ability = 1000000
n = 6
arr = list(map(int, input().split()))

# 각팀의 능력차이 계산
def diff(i, j, k, l):
    # 첫번째+두번째 팀원합 빼주면 세번째 팀원합 나옴
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 - sum2
    # 세팀의 차이 중 최댓값 리턴
    ret = abs(sum1 - sum2)
    ret = max(ret, abs(sum2-sum3))
    ret = max(ret, abs(sum1-sum3))

    return ret

min_diff = max_ability
# 첫번째 팀원만들기
for i in range(n):
    for j in range(i+1, n):
        # 두번째 팀원만들기
        for k in range(n):
            for l in range(k+1, n):
                # 첫번째 팀원과 두번째 팀원 겹치는지 확인
                if k == i or k == j or l == i or l == j:
                    continue
                # 안겹치면
                min_diff = min(min_diff, diff(i,j,k,l))

print(min_diff)