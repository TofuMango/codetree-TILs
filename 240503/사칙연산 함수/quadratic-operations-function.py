a,o,c = input().split()

def car(a,b,c):
    a = int(a)
    c = int(c)
    if b == '+':
        return print(a, "+", c, "=", a+c)
    elif b == '-':
        return print(a, "-", c, "=", a-c)
    elif b == '/':
        return print(a, "/", c, "=", int(a/c))
    elif b == '*':
        return print(a, "*", c, "=", a*c)
    else:
        print("False")

car(a,o,c)