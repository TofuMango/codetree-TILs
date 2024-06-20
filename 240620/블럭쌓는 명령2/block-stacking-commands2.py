n, k = tuple(map(int, input().split()))
# max값을 구하기 위한 1차원 배열 선언 후 초기화
res = []
for i in range(n):
    res.append(0)
# k번 만큼 반복
for i in range(k):
    a, b = tuple(map(int, input().split()))
    for num in range(b-a+1):
        res[a+num]+=1
print(max(res))