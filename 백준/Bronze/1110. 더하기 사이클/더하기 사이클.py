def new_num(n):
    a = n // 10
    b = n % 10
    new = a + b
    n = 10*b + new % 10
    return n


N = int(input())
end = N
cnt = 0
while True:
    N = new_num(N)
    cnt += 1
    if N == end:
        break
print(cnt)
