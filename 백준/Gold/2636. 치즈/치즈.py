from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N, M = map(int, input().split())
Cheese = [list(map(int, input().split())) for _ in range(N)]


def find():
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    cnt = 0

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if Cheese[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

                elif Cheese[ny][nx] == 1:
                    Cheese[ny][nx] = 0
                    visited[ny][nx] = 1
                    cnt += 1
    last.append(cnt)
    return cnt


time = 0
last = []
while True:
    cheese = find()
    time += 1
    if cheese == 0:
        break
print(time-1)
print(last[-2])