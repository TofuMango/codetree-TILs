# 날짜
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# 월
month = [31,29,31,30,31,30,31,31,30,31,30,31]
# 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))
day = input()
# 횟수세기
cnt = 0
index = 0
# day를 인덱스화 시키기
for i in range(len(day_list)):
    if day == day_list[i]:
        index = i
while True:
    # 만약 d1이 31, 30일 이러면 다음달로 넘어가
    if d1 == month[m1-1]:
        d1 = 1
        m1 += 1
    # 아니면 d1을 1씩더하고
    else:
        d1 += 1
        # 만약 날짜가 Sat라면 cnt += 1하기
        if d1%7 == index or d1 == index:
            cnt += 1
    if d1 == d2 and m1 == m2:
        if d1%7 == index or d1 == index:
            cnt += 1
        print(cnt+1)
        break