# 날짜와 월 입력 받기
m1, d1, m2, d2 = map(int, input().split())
day_input = input()

# 요일 리스트
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 각 월의 일수
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 시작 요일을 인덱스로 변환
day_index = day_list.index(day_input)

# 누적 일수 계산
total_days = 0
for month in range(m1 - 1):
    total_days += month_days[month]
total_days += d1

# 카운트와 현재 요일 인덱스 초기화
count = 0
current_day_index = day_index

# 날짜 세기 시작
while not (m1 == m2 and d1 == d2):
    if current_day_index == day_index:
        count += 1
    # 다음 날로 이동
    d1 += 1
    if d1 > month_days[m1 - 1]:
        d1 = 1
        m1 += 1
    # 요일 인덱스 업데이트
    current_day_index = (current_day_index + 1) % 7

# 마지막 날짜 포함 여부 확인
if current_day_index == day_index:
    count += 1

print(count)