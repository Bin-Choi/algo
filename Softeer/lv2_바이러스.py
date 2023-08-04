import sys
sys.stdin = open("input.txt", "r")

K, P, N = map(int, input().split())

dp = [0] * (N+1)
dp[0] = K

for i in range(1, N+1):
    dp[i] = (dp[i-1]*P) % 1000000007

print(dp[N])