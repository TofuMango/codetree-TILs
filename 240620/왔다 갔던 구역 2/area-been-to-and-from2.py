offerset = 300
max_space = 600
n = int(input())
segment = [
    tuple(input().split())
    for _ in range(n)
]
res = [0] * (max_space+1)
# res[100]의 위치부터 시작
for x, y in segment:
    x = int(x)
    # 만약 y가 R이라면 
    if y == 'R':
        for i in range(x):
            res[offerset+i]+=1
        offerset+=x
            
    if y == 'L':
        for i in range(x):
            res[offerset-i]+=1
        offerset-=x
cnt = 0
for r in res:
    if r >= 2:
        cnt += 1
print(cnt)