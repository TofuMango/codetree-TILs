# 입력
arr = tuple(input())
n = len(arr)
# 쌍의 수 카운팅
match_chr = 0
for i in range(n):
        for j in range(i+1, n):
            if arr[i] == '(' and arr[j] == ')':
                match_chr += 1
print(match_chr)
# 얘는 완탐이 아니군...?
# # 입력
# arr = tuple(input())
# n = len(arr)
# # 쌍의 수 카운팅
# match_chr = 0
# for i in range(n):
#     if arr[i] == '(':
#         for j in range(i+1, n):
#             if arr[j] == ')':
#                 match_chr += 1
# print(match_chr)