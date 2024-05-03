y = int(input())

def year(n):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True
    return False

if year(y):
    print("true")
else:
    print("false")