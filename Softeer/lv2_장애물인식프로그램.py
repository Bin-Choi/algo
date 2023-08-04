import sys
sys.stdin = open("input.txt", "r")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(s, e):
    stk = [(s, e)]
    cnt = 1
    arr[s][e] = 2
    while stk:
        x, y = stk.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny <N:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 2
                    cnt += 1
                    stk.append((nx, ny))

    block.append(cnt)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
block = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i, j)

block.sort()
print(len(block))
for b in block:
    print(b)

