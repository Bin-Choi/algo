import sys
sys.stdin = open("input.txt", "r")

N = int(input())
S = [0]
D = list([0] * 2 for _ in range(N+1))

for _ in range(N):
    S.append(int(input()))

D[1][0] = S[1]
D[1][1] = 0
if N >= 2:
    D[2][0] = S[2]
    D[2][1] = S[1]+S[2]

for i in range(3, N+1):

    D[i][0] = max(D[i-2][0], D[i-2][1]) + S[i]
    D[i][1] = D[i-1][0] + S[i]

print(max(D[N][0], D[N][1]))
