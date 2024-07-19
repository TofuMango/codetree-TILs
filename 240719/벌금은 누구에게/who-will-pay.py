n, m, k = tuple(map(int, input().split()))
manage = [0 for _ in range(n)]
first = -1

for i in range(m):
    memberIndex = int(input()) - 1  # 인덱스는 0부터 시작하므로 -1
    manage[memberIndex] += 1
    if k == manage[memberIndex]:
        first = memberIndex + 1  # 출력은 1부터 시작하는 인덱스로 하기 위해 +1

print(first)