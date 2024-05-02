def print_rect(n, m):
    for _ in range(n):
        print("1" * m)

row_n, col_m = tuple(map(int, input().split()))
print_rect(row_n, col_m)