import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬 Tagging
def bfs1(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    Vis[a][b] = True
    Arr[a][b] = cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and Arr[nx][ny] == 1 and not Vis[nx][ny]:
                Vis[nx][ny] = True
                Arr[nx][ny] = cnt
                q.append((nx, ny))


def bfs2(num):
    global Min
    dist = [[-1] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            #  출발 섬
            if Arr[i][j] == num:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 섬 밖이면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 땅을 만나면 최소값 비교
            if Arr[nx][ny] > 0 and Arr[nx][ny] != num:
                Min = min(Min, dist[x][y])
                return

            # 간 적없는 바다
            if Arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]
Vis = [[False] * N for _ in range(N)]
# 최솟값 비교를 위한 최대값 설정 == float('INF')
Min = sys.maxsize

# 섬 번호 Tag
cnt = 1
for i in range(N):
    for j in range(N):
        if Arr[i][j] == 1 and not Vis[i][j]:
            bfs1(i, j)
            cnt += 1

# 섬과 섬 최소 거리 구하기
for i in range(1, cnt):
    bfs2(i)

print(Min)