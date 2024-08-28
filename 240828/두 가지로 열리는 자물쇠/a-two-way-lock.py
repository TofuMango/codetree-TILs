n = int(input())
comb1 = list(map(int, input().split()))
comb2 = list(map(int, input().split()))
# 조건 확인
def check(i,j,k):
    # 첫번째 조합에서 확인
    a1 = min(abs(comb1[0] - i), n - abs(comb1[0] - i))
    a2 = min(abs(comb1[1] - j), n - abs(comb1[1] - j))
    a3 = min(abs(comb1[2] - k), n - abs(comb1[2] - k))
    # 두번째 조합에서 확인
    b1 = min(abs(comb2[0] - i), n - abs(comb2[0] - i))
    b2 = min(abs(comb2[1] - j), n - abs(comb2[1] - j))
    b3 = min(abs(comb2[2] - k), n - abs(comb2[2] - k))
    if a1 <= 2 and a2 <= 2 and a3 <= 2:
        return 1
    elif b1 <= 2 and b2 <= 2 and b3 <= 2:
        return 1
    else:
        return 0

# 합계 구하기
cnt = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            cnt += check(i,j,k)
print(cnt)