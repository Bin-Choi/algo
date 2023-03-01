import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(input().rstrip()))
    if 'J' in arr[i]:
        q = deque([(0, i, arr[i].index('J'))])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'F':
            q.append((-1, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 'IMPOSSIBLE'

while q:
    time, x, y = q.popleft()
    # 탈출
    if time > -1 and arr[x][y] != 'F' and (x == 0 or y == 0 or x == n-1 or y == m-1):
        ans = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#':

            # 이동
            if time > -1 and arr[nx][ny] == '.':
                arr[nx][ny] = '_'
                q.append((time+1, nx, ny))

            # 불 확산
            elif time == -1 and arr[nx][ny] != 'F':
                arr[nx][ny] = 'F'
                q.append((-1, nx, ny))

print(ans)
