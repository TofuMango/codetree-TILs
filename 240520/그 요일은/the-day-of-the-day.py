def count_days(m1, d1, m2, d2, A):
    # 요일 리스트
    day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # 각 월의 일수 (2024년은 윤년)
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 시작 요일부터 A까지 며칠이 필요한지 계산
    start_day_index = 0  # 월요일
    target_day_index = day_list.index(A)
    days_to_target = (target_day_index - start_day_index) % 7
    
    # 시작 날짜와 끝 날짜 사이의 총 일수 계산
    total_days = d2 - d1  # 시작 월의 일수 차이
    for month_index in range(m1, m2):
        total_days += month_days[month_index - 1]  # 시작 월과 끝 월 사이의 전체 일수 추가
    
    # 시작일로부터 A 요일까지 며칠이 필요한지 고려하여 첫 번째 A 요일 계산
    if days_to_target > total_days % 7:
        first_A_day = days_to_target - (total_days % 7)
    else:
        first_A_day = 0
    
    # A 요일이 등장하는 횟수 계산
    if total_days >= days_to_target:
        return ((total_days - days_to_target) // 7) + 1
    else:
        return 0

# 입력
m1, d1, m2, d2 = map(int, input().split())
A = input()

# 결과 출력
print(count_days(m1, d1, m2, d2, A))