# 입력
arr = tuple(input())
n = len(arr)
# 쌍의 수 카운팅
match_chr = 0
for i in range(n):
    if arr[i] == '(':
        for j in range(i+1, n):
            if arr[j] == ')':
                match_chr += 1
print(match_chr)