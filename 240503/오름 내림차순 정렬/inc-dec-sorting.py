n = int(input())
listN = list(map(int, input().split()))

# 오름차순으로 정렬 후 바로 출력
listN.sort()
for i in listN:
    print(i, end=" ")
print()  # 줄바꿈

# 내림차순으로 정렬 후 바로 출력
listN.sort(reverse=True)
for i in listN:
    print(i, end=" ")