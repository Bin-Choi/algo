import sys
sys.stdin = open("input.txt", "r")
N = int(input())
arr = [[0] * 101 for _ in range(101)]
I = []
J = []
for square in range(N):
    si, sj, ei, ej = map(int, input().split())
    I.append([si, ei])
    J.append([sj, ej])
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] += 1

for sq in range(N):
    cnt = 0
    for i in range(I[sq][0], I[sq][1]):
        for j in range(J[sq][0], J[sq][1]):
            if arr[i][j] == 1:
                cnt += 1
    print(cnt)
#
