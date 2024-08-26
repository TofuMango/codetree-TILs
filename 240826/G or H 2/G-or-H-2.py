MAX_NUM = 100 

n = int(input())
# dp 처럼 우선 만들어두기 
arr = [0] * (MAX_NUM + 1) 

for _ in range(n):
    x,c = input().split()
    x = int(x)

    if c == 'G':
        arr[x] = 1 
    elif c== 'H':
        arr[x] = 2

max_len = 0 
for i in range(MAX_NUM+1):
    for j in range(i+1,MAX_NUM+1):
        # i 와 j 위치에 사람이 있는지 확인 
        if arr[i] == 0 or arr[j] == 0:
            continue
        
        cnt_g = 0
        cnt_h = 0
        
        for k in range(i,j+1):
            if arr[k] == 1:
                cnt_g += 1 
            if arr[k] == 2:
                cnt_h += 1 
        
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            length = j - i 
            max_len = max(max_len,length)

print(max_len)
# max_len = 100
# n = int(input())
# arr = [0] * (max_len + 1)

# # 바구니에 사람 수와 중요도 입력 받기
# for _ in range(n):
#     people, impo = input().split()
#     people = int(people)
#     arr[people] = impo  # arr에 'G' 또는 'H' 저장

# # 최대 크기 구하기
# max_size = 0

# # 모든 구간 확인
# for i in range(max_len + 1):
#     for j in range(i, max_len + 1):
#         G = 0
#         H = 0
#         size = 0
        
#         # i부터 j까지의 구간 확인
#         for k in range(i, j + 1):
#             if arr[k] == 'G':
#                 G += 1
#             elif arr[k] == 'H':
#                 H += 1

#         # 조건에 따라 size 계산
#         if G != 0 and H == 0:
#             size = G  # G로만 이루어져있다면
#         elif H != 0 and G == 0:
#             size = H  # H로만 이루어져있다면
#         elif G == H:
#             size = G + H  # G와 H 비율이 같다면

#         max_size = max(max_size, size)

# print(max_size)