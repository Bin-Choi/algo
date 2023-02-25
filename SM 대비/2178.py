import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and Map[nx][ny] == 1:
                q.append((nx, ny))
                Map[nx][ny] = Map[x][y] + 1

    return Map[n-1][m-1]


n, m = map(int, input().split())
Map = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = bfs(0, 0)
print(ans)