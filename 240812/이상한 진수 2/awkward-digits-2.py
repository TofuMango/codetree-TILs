# 입력을 받아 리스트로 변환
bin_list = list(map(int, input()))  
max_num = 0

for i in range(len(bin_list)):
    # 현재 위치의 값을 바꿔서 새로운 숫자를 만들어보는 과정
    if bin_list[i] == 0:  # 0을 1로 바꾸는 경우
        bin_list[i] = 1
        number = int(''.join(map(str, bin_list)))  # 리스트를 문자열로 변환 후 정수로 변환
        max_num = max(max_num, number)  # 최대값 갱신
        bin_list[i] = 0  # 원래 값으로 복구
    else:  # 1인 경우 1을 0으로 변경
        bin_list[i] = 0
        number = int(''.join(map(str, bin_list)))  # 리스트를 문자열로 변환 후 정수로 변환
        max_num = max(max_num, number)  # 최대값 갱신
        bin_list[i] = 1  # 원래 값으로 복구

# max_num이 이진수 형태로 저장되어 있으므로 10진수로 변환
ans = int(str(max_num), 2)  # 이진수 문자열을 10진수로 변환

print(ans)  # 10진수 값 출력