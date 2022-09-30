import sys
sys.stdin = open("input.txt", "r")

INF = 100*100*10
def bfs(si,sj):
    q = []
    s = [[INF]*N for _ in range(N)]

    q.append((si, sj))
    s[si][sj] = 0
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and s[ci][cj]+MAP[ni][nj] < s[ni][nj]:
                s[ni][nj] = s[ci][cj] + MAP[ni][nj]
                q.append((ni,nj))



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0,0)

