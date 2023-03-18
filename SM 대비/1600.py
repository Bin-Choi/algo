import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][z]-1

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][z] and not arr[nx][ny]:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append([nx, ny, z])

        if z < K:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][z+1] and not arr[nx][ny]:
                    visited[nx][ny][z+1] = visited[x][y][z]+1
                    q.append([nx, ny, z+1])

    return -1


K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]
hx = [2, 1, -1, -2, -2, -1, 1, 2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]

Min = bfs()
print(Min)
