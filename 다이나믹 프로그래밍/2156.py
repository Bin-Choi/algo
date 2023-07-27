import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = [0] * 10001
dp = [0] * 10001
for i in range(1, N+1):
    lst[i] = int(input())

dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
dp[3] = max(dp[1]+lst[3], dp[0]+lst[2]+lst[3], dp[2])

for i in range(4, N+1):
    dp[i] = max(dp[i-1], dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])

print(dp[N])