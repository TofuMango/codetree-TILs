import sys
INT_MIN = -sys.maxsize

# 변수선언
binary = list(map(int, list(input())))
# 이게나은듯?
# binary = list(map(int, input()))
length = len(binary)
# i번쨰 자릿수 바꾸었을때 십진수값 구하기
ans = INT_MIN
for i in range(length):
    # i번째 자릿수 바꾸기
    # 만약 i가 0이라면 1이될거고,, 1이면 0이됨
    binary[i] = 1 - binary[i]
    # 십진수로 변환하기
    num = 0
    for j in range(length):
        num = num * 2 + binary[j]
    ans = max(ans, num)
    # 자리수 원래대로 돌려놓기
    binary[i] = 1- binary[i]
# 출력
print(ans)

# 똑같긴한데 더 복잡해..
# # 입력을 받아 리스트로 변환
# bin_list = list(map(int, input()))  
# max_num = 0

# for i in range(len(bin_list)):
#     # 현재 위치의 값을 바꿔서 새로운 숫자를 만들어보는 과정
#     if bin_list[i] == 0:  # 0을 1로 바꾸는 경우
#         bin_list[i] = 1
#         number = int(''.join(map(str, bin_list)))  # 리스트를 문자열로 변환 후 정수로 변환
#         max_num = max(max_num, number)  # 최대값 갱신
#         bin_list[i] = 0  # 원래 값으로 복구
#     else:  # 1인 경우 1을 0으로 변경
#         bin_list[i] = 0
#         number = int(''.join(map(str, bin_list)))  # 리스트를 문자열로 변환 후 정수로 변환
#         max_num = max(max_num, number)  # 최대값 갱신
#         bin_list[i] = 1  # 원래 값으로 복구

# # max_num이 이진수 형태로 저장되어 있으므로 10진수로 변환
# ans = int(str(max_num), 2)  # 이진수 문자열을 10진수로 변환

# print(ans)  # 10진수 값 출력