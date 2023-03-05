import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])
    arr[sx][sy] = 1

    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            return arr[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])




T = int(input())

dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]

for test in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    arr = [[0] * n for _ in range(n)]

    ans = bfs(sx, sy, ex, ey)
    print(ans)

