import sys
sys.stdin = open("input.txt", "r")

di = [-1, 1]
dj = [1, -1]

M, N = map(int, input().split())
arr = [[0]*M for _ in range(N)]
gj, gi = map(int, input().split())
H = int(input())
si = N - gi
sj = gj
move1 = move2 = d1 = d2 = 0
print(si, sj)
while move1 <= H:
    ni = si + di[d1]
    if 0 <= ni < N and arr[ni][sj] == 0:
        si = ni
        move1 += 1
    else:
        d1 = (d1 + 1) % 2
        move1 += 1
while move2 <= H:
    nj = sj + dj[d2]
    if 0 <= nj < M and arr[si][nj] == 0:
        sj = nj
        move2 += 1
    else:
        d2 = (d2 + 1) % 2
        move2 += 1

print(ni, nj)
