# max_ability = 1000000
# n = 6
# arr = list(map(int, input().split()))

# # 각팀의 능력차이 계산
# def diff(i, j):
#     res = abs(arr[i]-arr[j])
#     return res

# min_diff = max_ability
# for i in range(n):
#     # 능력차이 합계 
#     sum_diff = 0
#     for j in range(i+1, n):
#         a_sum = diff(i,j)
#     min_diff = min(sum_diff, min_diff)

from itertools import combinations

# 입력 처리
arr = list(map(int, input().split()))

# 가능한 모든 팀 조합을 생성
team_combinations = list(combinations(range(6), 2))

min_diff = float('inf')

# 팀 조합을 통해 모든 가능한 팀을 만들고 능력 총합을 계산
for team1 in team_combinations:
    remaining = [i for i in range(6) if i not in team1]
    
    # 나머지 팀 조합을 통해 팀 2와 팀 3을 생성
    for team2 in combinations(remaining, 2):
        team3 = [i for i in remaining if i not in team2]
        
        # 각 팀의 능력 총합 계산
        sum_team1 = arr[team1[0]] + arr[team1[1]]
        sum_team2 = arr[team2[0]] + arr[team2[1]]
        sum_team3 = arr[team3[0]] + arr[team3[1]]
        
        # 최대 팀과 최소 팀의 능력 총합 계산
        max_sum = max(sum_team1, sum_team2, sum_team3)
        min_sum = min(sum_team1, sum_team2, sum_team3)
        
        # 차이를 구하여 최소값 업데이트
        min_diff = min(min_diff, max_sum - min_sum)

print(min_diff)