import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs():
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1
    arr[0][0] = 1
    # 시작 지점 스위치 켜주기
    for a, b in light[0][0]:
        arr[a][b] = 1

    while q:
        i, j = q.popleft()

        for dir in range(4):
            ni = i + dx[dir]
            nj = j + dy[dir]
            if not(0 <= ni < n and  0 <= nj < n):
                continue

            if visit[ni][nj] == 0 and arr[ni][nj] == 1:
                visit[ni][nj] = 1
                q.append((ni, nj))

                # 들어간 방의 스위치 켜주기
                for a, b in light[ni][nj]:
                    arr[a][b] = 1

                    # 스위치 켜진 방으로 갈 수 있다면 넣기
                    for dir in range(4):
                        na = a + dx[dir]
                        nb = b + dy[dir]

                        if not(0 <= na < n and 0 <= nb < n):
                            continue

                        if arr[na][nb] == 1 and visit[na][nb] == 1:
                            q.append((na, nb))

    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                ans += 1

    return ans


n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
light = [[[] for _ in range(n)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1

    light[x][y].append((a, b))

print(bfs())

