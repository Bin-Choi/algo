import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
S = list(map(int, input().split()))
D = [0] * 100001
D[1] = S[0]
for i in range(2, N+1):
    D[i] = D[i-1] + S[i-1]

for test in range(M):
    i, j = map(int, input().split())
    print(D[j] - D[i-1])







