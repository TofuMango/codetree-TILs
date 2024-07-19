# n, m, k = tuple(map(int, input().split()))
# manage = [0 for _ in range(n+1)]
# first = -1

# for i in range(m):
#     memberIndex = int(input())
#     manage[memberIndex] += 1
#     # 이미 횟수에 도달하면 카운팅되지않도록 first==-1조건추가
#     if k == manage[memberIndex] and first == -1:
#         first = memberIndex
# print(first)
# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))
penalized_person = [
    int(input())
    for _ in range(m)
]
penalty_num = [0] * (n + 1)

# 각 패널티 횟수를 세서,
# 최초로 K번 이상 벌칙을 받는 사람을 추적
ans = -1
for target in penalized_person:
    penalty_num[target] += 1

    if penalty_num[target] >= k:
        ans = target
        break

print(ans)