arr_2d = [
    list(map(str, input().split()))
    for a in range(5)
]


for a,b,c in arr_2d:
    print(a.upper(),b.upper(),c.upper())