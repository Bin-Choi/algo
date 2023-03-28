import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs():
    is_move = True
    while is_move:
        is_move = False

        for i in range(1, p+1):
            if not castle[i]:
                continue
            q = castle[i]
            for _ in range(s[i]):
                if not q:
                    break
                for _ in range(len(q)):
                    x, y = q.popleft()

                    for v in range(4):
                        nx = x+dx[v]
                        ny = y+dy[v]

                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
                            arr[nx][ny] = str(i)
                            q.append((nx, ny))
                            cnt[i] += 1
                            is_move = True


n, m, p = map(int, input().split())
s = [0]+list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(n)]
cnt = [0] * (p+1)
castle = [deque() for _ in range(p+1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 시작 성 위치 등록
for i in range(n):
    for j in range(m):
        if arr[i][j] != '.' and arr[i][j] != '#':
            cnt[int(arr[i][j])] += 1
            castle[int(arr[i][j])].append((i, j))

bfs()
print(*cnt[1:])






