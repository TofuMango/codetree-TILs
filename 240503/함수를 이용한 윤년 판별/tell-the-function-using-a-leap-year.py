y = int(input())

def year(n):
    if y % 4 == 0:
        return True
    if y % 100 == 0 and y % 400 != 0:
        return False
    return False

if year(y):
    print("true")
else:
    print("false")