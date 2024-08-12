n = int(input())
arr = list(map(int, input().split()))
res = []
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] < arr[j] and arr[j] < arr[k]:
                res.append(str(arr[i])+str(arr[j])+str(arr[k]))
unique_res = set(res)
cnt = len(unique_res)
print(cnt)