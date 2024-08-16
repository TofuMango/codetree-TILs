n = int(input())
arr = list(input().strip())  # 문자열을 리스트로 변환 (공백 없이)
cnt = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] == 'C' and arr[j] == 'O' and arr[k] == 'W':
                cnt += 1

print(cnt)