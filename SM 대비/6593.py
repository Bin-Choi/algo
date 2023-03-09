from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def bfs(i, j, k):
    q = deque()
    q.append((i, j, k, 0))
    visited[i][j][k] = 1

    while q:
        z, y, x, cnt = q.popleft()

        if tower[z][y][x] == 'E':
            return cnt
        cnt += 1

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and visited[nz][ny][nx] == 0:
                if tower[nz][ny][nx] == '.' or tower[nz][ny][nx] == 'E':
                    visited[nz][ny][nx] = 1
                    q.append((nz, ny, nx, cnt))

    return -1


dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    tower = []
    visited = [[[0]*c for _ in range(r)]for _ in range(l)]
    for _ in range(l):
        tower.append([list(input().strip()) for _ in range(r)])
        temp = input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if tower[i][j][k] == 'S':
                    ans = bfs(i, j, k)


    if ans == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {ans} minute(s).')



