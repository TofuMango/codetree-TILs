# 풀이1
# arr_2d = [
#     list(map(str, input().split()))
#     for a in range(5)
# ]


# for a,b,c in arr_2d:
#     print(a.upper(),b.upper(),c.upper())

# 풀이2
arr_2d = [
    list(input().split())
    for _ in range(5)
]

for i in range(5):
    for j in range(3):
        # 아스키코드 A는 65 a는 97, 65-97 = -32, 대문자와 소문자 사이의 아스키 코드 차이가 -32, 이는 소문자를 대문자로 변경해줌
        # 대문자의 경우 아스키 코드가 소문자보다 32 작기 때문!
        arr_2d[i][j]=chr(ord(arr_2d[i][j])+ord('A')-ord('a'))
        print(arr_2d[i][j], end=" ")
    print()