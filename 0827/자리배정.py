import sys
sys.stdin = open("input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
R, C = map(int, input().split())
arr = [[0] * R for _ in range(C)]
p = int(input())
si = C - 1
sj = 0
d = 0
err = 0
cnt = 1
arr[si][sj] = cnt
cnt += 1
while cnt <= p:
    if p > C * R:
        err = 1
        break
    ni, nj = si + di[d], sj + dj[d]
    if 0 <= ni < C and 0 <= nj < R and arr[ni][nj] == 0:
        si, sj = ni, nj
        arr[si][sj] = cnt
        cnt += 1
    else:
        d = (d + 1) % 4

if err != 1:
    ai = sj + 1
    aj = C - si
    print(ai, aj)
else:
    if p == 1:
        print(1, 1)
    else:
        print(err)
