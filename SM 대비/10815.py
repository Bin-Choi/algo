import sys
sys.stdin = open("input.txt", "r")

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


Plus = [0] * 10000000
Minus = [0] * 10000000
ans = [0] * M

for n in range(N):
    if A[n] >= 0:
        Plus[A[n]] = 1
    else:
        Minus[A[n]] = 1

for m in range(M):
    if (B[m] >= 0 and Plus[B[m]] == 1) or (B[m] < 0 and Minus[B[m]] == 1) :
        ans[m] = 1

print(*ans)

