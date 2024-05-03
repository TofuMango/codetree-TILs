a,o,c = input().split()

def car(a,b,c):
    a = int(a)
    c = int(c)
    if b == '+':
        return a + c
    if b == '-':
        return a - c
    if b == '/':
        return a / c
    if b == '*':
        return a * c

print(a, o, c, "=", car(a,o,c))