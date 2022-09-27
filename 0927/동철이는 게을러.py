import sys
sys.stdin = open("input.txt", "r")


def gowork(n, pr):
    global mx
    if pr <= mx:
        return
    if n == N:
        mx = max(pr, mx)
        return
    for i in range(N):
        if work[i] == 0:
            work[i] = 1
            gowork(n+1, pr*lst[n][i]*0.01)
            work[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    work = [0] * N
    mx = 0
    gowork(0, 1)

    print(f'#{test_case} %.6f'%(mx*100))