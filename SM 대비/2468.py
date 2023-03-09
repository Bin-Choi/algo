import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(i, j, h):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] > h:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0

for i in range(N):
    Max = max(Map[i])

for h in range(Max):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h)
                cnt += 1
    ans = max(ans, cnt)

print(ans)