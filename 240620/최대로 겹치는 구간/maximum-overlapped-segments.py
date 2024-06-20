OFFSET = 100
# 100을 더하고 진행하기때문에 [0,200]내의 최댓값을 구하게됨 그래서 max값을 200으로 줌
MAX_R = 200
# 입력
n = int(input())
seg = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
check = [0] * (MAX_R+1)
# offset을 적용하여 음수인 수를 양수로 변환해줌
for x1, x2 in segments:
    x1, x2 = x1+OFFSET, x2+OFFSET
    # 구간 칠해주기
    # 만약 [1, 5]였다 하면 구간은 1-2, 2-3, 3-4, 4-5가 칠해져야 하므로 1,2,3,4 에 카운트해줘야함 그러니까 x1, x2-1 이 되도록 해주면 됨
    # for 문이므로 x1 ~ x2-1임
    for i in range(x1, x2):
        check[i]+=1

# 최댓값 구하기
max_num = max(check)
print(max_num)