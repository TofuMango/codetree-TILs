max_ability = 1000
n = 5
arr = list(map(int, input().split()))
# 능력의 합 구하기
def diff(i,j,k,l):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 - sum2
    if sum1 != sum2 and sum2 != sum3 and sum1 != sum3:
        # 세팀의 차이 중 최댓값 리턴
        ret = abs(sum1-sum2)
        ret = max(ret, abs(sum2-sum3))
        ret = max(ret, abs(sum3-sum1))
        return ret
    else:
        return max_ability

min_diff = max_ability
# 첫번째 팀
for i in range(n):
    for j in range(i+1, n):
        # 두번째 팀
        for k in range(n):
            for l in range(k+1, n):
                # 첫번째 팀과 두번째 팀 팀원겹치는지 확인
                if k == i or k == j or l == i or l == j:
                    continue
                min_diff = min(min_diff, diff(i,j,k,l))
            
if min_diff == max_ability:
    print(-1) 
else:
    print(min_diff)