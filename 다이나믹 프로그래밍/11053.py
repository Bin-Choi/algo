import sys
sys.stdin = open("input.txt", "r")

n = int(input())
dp = [0] * (n+1)
lst = [0] + list(map(int, input().split()))

dp[1] = 1
for i in range(1, n+1):
    mx = 0
    for j in range(0, i):
        if lst[i] > lst[j]:
            mx = max(dp[j], mx)
    dp[i] = mx + 1

print(max(dp))
