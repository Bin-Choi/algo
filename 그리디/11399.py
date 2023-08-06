import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = list(map(int, input().split()))
dp = [0]*N
lst.sort()

dp[0] = lst[0]
for i in range(1, N):
    dp[i] = dp[i-1] + lst[i]

print(sum(dp))

ans = 0
for i in range(0, N):
    ans += (N-i) * lst[i]

print(ans)