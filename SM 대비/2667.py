import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and Arr[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt


N = int(input())
Arr = []
visited = [[0] * N for _ in range(N)]
ans = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    Arr.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if Arr[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print(*ans)