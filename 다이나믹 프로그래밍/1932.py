import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]
D = []
for i in range(1, N+1):
    D.append([0]*i)

D[0] = S[0]
if N >= 2:
    D[1][0] = D[0][0] + S[1][0]
    D[1][1] = D[0][0] + S[1][1]

for i in range(2, N):
    for j in range(i+1):
        if j == 0:
            D[i][j] = D[i-1][j] + S[i][j]
        elif j == i:
            D[i][j] = D[i-1][j-1] + S[i][j]
        else:
            D[i][j] = max(D[i-1][j-1], D[i-1][j]) + S[i][j]

print(D)
