# class 정의
class product_inform:
    def __init__(self, product="codetree", code=50):
        self.product = product
        self.code = code
# 입력
i_product, i_code = input().split()
# 객체 생성
pd1 = product_inform()
pd2 = product_inform(i_product, i_code)
# 출력
print(f"product {pd1.code} is {pd1.product}")
print(f"product {pd2.code} is {pd2.product}")