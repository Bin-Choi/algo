import sys
sys.stdin = open("input.txt", "r")


def bt(n, sm):
    global mn
    # 종료조건
    if n == N:
        mn = min(sm, mn)
        return
    # 가지치기
    if sm >= mn:
        return
    # 재귀호출
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            bt(n+1, sm + arr[n][i])
            visited[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    mn = 100 * 15
    bt(0, 0)

    print(f'#{test_case} {mn}')

