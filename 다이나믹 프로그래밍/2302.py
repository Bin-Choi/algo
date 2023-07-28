import sys
sys.stdin = open("input.txt", "r")

N = int(input())
M = int(input())
dp = [0] * (N + 1)
v = [0] * (N + 1)

for i in range(M):
    v[int(input())] = 1

dp[1] = 1
if N > 1:
    if v[1] or v[2]:
        dp[2] = 1
    else:
        dp[2] = 2

if N > 2:
    for i in range(3, N + 1):
        if v[i] or v[i - 1]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])