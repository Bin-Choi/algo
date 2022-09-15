import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = [0 for _ in range(N + 1)]

    for i in range(M):
        n, v = map(int, input().split())
        lst[n] = v

    for i in range(N, 0, -1):
        if i // 2 > 0:
            lst[i // 2] += lst[i]

    print('#{} {}'.format(test_case, lst[L]))
