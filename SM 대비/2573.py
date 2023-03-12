import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if Map[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                else:
                    cnt[x][y] += 1

    return 1


N, M = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
year = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    visited = [[False] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0 and not visited[i][j]:
                ans.append(bfs(i, j))

    for i in range(N):
        for j in range(M):
            Map[i][j] -= cnt[i][j]
            if Map[i][j] < 0:
                Map[i][j] = 0

    if len(ans) == 0 or len(ans) >= 2:
        break

    year += 1

print(year) if len(ans) >= 2 else print(0)