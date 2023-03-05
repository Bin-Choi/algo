import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(X, Y):
    q.append((X, Y))
    visited[X][Y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and Arr[x][y] == Arr[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


N = int(input())
Arr = [list(input()) for _ in range(N)]
ans1, ans2 = 0, 0
visited = [[0] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            ans1 += 1

for i in range(N):
    for j in range(N):
        if Arr[i][j] == 'G':
            Arr[i][j] = 'R'

q = deque()
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            ans2 += 1

print(ans1, ans2)

