import sys
sys.stdin = open("input.txt", "r")


def solve(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


for time in range(int(input())):

    m, n, x, y = map(int, input().split())

    ans = solve(m, n, x, y)

    print(ans)
