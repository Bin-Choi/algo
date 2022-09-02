import sys
sys.stdin = open("input.txt", "r")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    C0 = C1 = 0
    if fibonacci(N) == 0:
        C0 += 1
    else:
        C1 += 1
    print(C0, C1)