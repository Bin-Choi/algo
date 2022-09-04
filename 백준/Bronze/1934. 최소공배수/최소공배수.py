def Gcd(m, a, b):
    for i in range(m, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


N = int(input())
for n in range(N):
    a, b = map(int, input().split())
    m = min(a, b)
    gcd = Gcd(m, a, b)
    lcm = a*b//gcd
    print(lcm)