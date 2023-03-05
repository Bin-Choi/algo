import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(X, Y):
    q = deque()
    q.append((X, Y))
    visited[X][Y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


T = int(input())
for test in range(T):
    m, n, k = map(int, input().split())

    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 셋팅
    for i in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)
