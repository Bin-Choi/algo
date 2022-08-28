import sys
sys.stdin = open("input.txt", "r")


def BFS(i, j):
    visited = [[0]*16 for _ in range(16)]
    q = []
    # 시작점 & 방문처리
    q.append([i, j])
    visited[i][j] = 1
    # while 돌리기
    while q:
        i, j = q.pop(0)
        if Map[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 > ni or 0 > nj or 16 <= ni or 16 <= nj:
                continue
            if visited[ni][nj] == 0 and Map[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = 1
    return 0


for test_case in range(1, 11):
    _ = input()
    Map = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if Map[i][j] == 2:
                si, sj = i, j

    ans = BFS(si, sj)

    print(f'#{test_case} {ans}')