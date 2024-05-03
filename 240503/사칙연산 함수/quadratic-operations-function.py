a,o,c = input().split()

def car(a,b,c):
    a = int(a)
    c = int(c)
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '/':
        return int(a / c)
    elif b == '*':
        return a * c
    else:
        print("False")

print(a, o, c, "=", car(a,o,c))