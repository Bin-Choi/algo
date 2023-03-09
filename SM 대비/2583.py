import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = 1
                    q.append([ny, nx])
                    cnt += 1
    return cnt


M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = []
# 색칠하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = -1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print(*ans)