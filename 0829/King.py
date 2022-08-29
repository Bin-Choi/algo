import sys
sys.stdin = open("input.txt", "r")

Map = [[0]*9 for _ in range(9)]
C = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
CC = {v: k for k, v in C.items()}
di = {'R': 1, 'L': -1, 'B': 0, 'T': 0, 'RT': 1, 'LT': -1, 'RB': 1, 'LB': -1}
dj = {'R': 0, 'L': 0, 'B': -1, 'T': 1, 'RT': 1, 'LT': 1, 'RB': -1, 'LB': -1}

K, S, N = map(str, input().split())
Ki, Kj = map(str, K)            # 킹, 돌 시작점
ki = C[Ki]
kj = int(Kj)
Si, Sj = map(str, S)
si = nsi = C[Si]
sj = nsj = int(Sj)
for n in range(int(N)):              # 동작
    d = input()
    ni = ki + di[d]
    nj = kj + dj[d]

    if ni == si and nj == sj:
        nsi = si + di[d]
        nsj = sj + dj[d]
        if 0 < nj < 9 and 0 < ni < 9 and 0 < nsi < 9 and 0 < nsj < 9:
            ki = ni
            kj = nj
            si = nsi
            sj = nsj
    else:
        if 0 < nj < 9 and 0 < ni < 9 :
            ki = ni
            kj = nj

Ki = CC[ki]
Si = CC[si]
Kj = str(kj)
Sj = str(sj)
print(Ki+Kj)
print(Si+Sj)