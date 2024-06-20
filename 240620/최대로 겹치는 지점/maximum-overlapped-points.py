max_imp = 100
n = int(input())
seg = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
res = [0] * (max_imp+1)
for x1, x2 in seg:
    for i in range(x1-1, x2):
        res[i]+=1
max_res = max(res)
print(max_res)