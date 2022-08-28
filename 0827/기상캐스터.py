import sys
sys.stdin = open("input.txt", "r")


def nextc(si, sj):
    for nj in range(1, W-sj):
        if ans[si][sj+nj] == 0:
            break
        else:
            ans[si][sj+nj] = nj


H, W = map(int, input().split())
Map = [list(map(str, input())) for _ in range(H)]
ans = [[-1]*W for _ in range(H)]
for i in range(H):                  # 구름 표시
    for j in range(W):
        if Map[i][j] == 'c':
            ans[i][j] = 0

for i in range(H):                  # 구름이 지나간다면, 시간 구하기
    for j in range(W):
        if ans[i][j] == 0:
            si, sj = i, j
            nextc(si, sj)

for p in range(H):
    print(*ans[p])

