# 정수입력
n = int(input())

# 정사각형 출력 함수
def square(N):
    num = 1
    for row in range(N):
        for col in range(N):
            if(num > 9):
                num = 1
            print(num, end=" ")
            num += 1
        print() 
        
# 출력
square(n)