import sys
sys.stdin = open("input.txt", "r")


def dfs(n, cnt, sm):
    global ans
    if ans <= cnt:
        return
    if n == N:
        ans = min(ans, cnt)
        return

    if sm>0:                        #교체하지 않는 경우
        dfs(n+1, cnt,sm-1)

    dfs(n+1, cnt+1, lst[n]-1)       #교체하는경우


T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N

    dfs(2, 0, lst[1]-1)

    print(f'#{test_case} {ans}')
