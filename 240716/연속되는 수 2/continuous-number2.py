n = int(input())
number = [0] * n
for i in range(n):
    tmp = int(input())
    number[i] = tmp
cnt = 0
max_cnt = 0
for i in range(n):
    cnt += 1
    # 그룹의 수..
    if number[i] == 0 or number[i] != number[i-1]:
        if cnt > max_cnt:
            max_cnt = cnt
            cnt = 0
print(max_cnt-1)