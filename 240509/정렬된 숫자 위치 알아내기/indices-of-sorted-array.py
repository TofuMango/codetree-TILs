# 클래스 선언
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index


# 변수 선언 및 입력
n = int(input())
numbers = []
arr = list(map(int, input().split()))
numbers = [
    Number(num, i)
    for i, num in enumerate(arr)
]
answer = [
    0 for _ in range(n)
]

# Custom Comparator를 활용한 정렬
numbers.sort(key=lambda x: (x.number, x.index))

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
for i, number in enumerate(numbers):
    answer[number.index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end = ' ')

# 수열의 길이 n
# n = int(input())
# # 수열 입력받기
# numList = list(map(int, input().split()))
# sortNum = sorted(numList)
# index = []
# # 인덱스 부여하기
# for i in enumerate(sortNum, start=1):
#     index.append(i)
# # index와 기존 수열 비교
# for i in range(n):
#     for j in range(n):
#         if(numList[i]== index[j][1]):
#             print(index[j][0], end=" ")
#         else:
#             continue