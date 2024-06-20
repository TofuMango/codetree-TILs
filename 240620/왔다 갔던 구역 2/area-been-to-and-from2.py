# 입력 받기
n = int(input())
commands = [input().split() for _ in range(n)]

# 위치 추적을 위한 딕셔너리 초기화
position_count = {}
current_position = 0

# 명령어 처리
for command in commands:
    distance = int(command[0])
    direction = command[1]
    
    if direction == 'R':
        for _ in range(distance):
            current_position += 1
            if current_position in position_count:
                position_count[current_position] += 1
            else:
                position_count[current_position] = 1
                
    elif direction == 'L':
        for _ in range(distance):
            current_position -= 1
            if current_position in position_count:
                position_count[current_position] += 1
            else:
                position_count[current_position] = 1

# 2번 이상 지나간 영역의 크기 계산
count_overlapping_areas = sum(1 for count in position_count.values() if count >= 2)

# 결과 출력
print(count_overlapping_areas)