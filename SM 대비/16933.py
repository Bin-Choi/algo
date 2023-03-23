import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, 0))
    vis[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return vis[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and z < k and vis[nx][ny][z+1] == 0:
                    if vis[x][y][z] % 2 == 1:
                        q.append((nx, ny, z+1))
                        vis[nx][ny][z+1] = vis[x][y][z] + 1
                    else:
                        q.append((nx, ny, z))
                        vis[nx][ny][z] = vis[x][y][z] + 1
                elif arr[nx][ny] == 0 and vis[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    vis[nx][ny][z] = vis[x][y][z] + 1

    return -1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, k = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
vis = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

print(bfs())