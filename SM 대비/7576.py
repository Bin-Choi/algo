import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                q.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1


m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 출발지 넣기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])

bfs()
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(arr[i]))
print(ans-1)

