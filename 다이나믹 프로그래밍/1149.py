import sys

sys.stdin = open("input.txt", "r")

N = int(input())
R = [0] * 1001
G = [0] * 1001
B = [0] * 1001
D = list([0] * 3 for _ in range(1001))

for i in range(1, N + 1):
    r, g, b = map(int, input().split())
    R[i] = r
    G[i] = g
    B[i] = b

D[1][0] = R[1]
D[1][1] = G[1]
D[1][2] = B[1]

for i in range(2, N + 1):
    D[i][0] = min(D[i - 1][1], D[i - 1][2]) + R[i]
    D[i][1] = min(D[i - 1][0], D[i - 1][2]) + G[i]
    D[i][2] = min(D[i - 1][0], D[i - 1][1]) + B[i]

print(min(D[N][0], D[N][1], D[N][2]))
