class Next:
    def __init__(self, A="codetree", B=10):
        self.A = A
        self.B = B

ID, Level = input().split()
Level = int(Level)

# 기본출력
check = Next()
print(f"user {check.A} lv {check.B}")
# 
check = Next(ID, Level)
print(f"user {check.A} lv {check.B}")