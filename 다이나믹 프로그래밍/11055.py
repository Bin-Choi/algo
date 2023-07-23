import sys
sys.stdin = open("input.txt", "r")

n = int(input())
Dp = [0] * (n+1)
lst = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    mx = 0
    for j in range(0, i):
        if lst[i] > lst[j]:
            mx = max(Dp[j], mx)
    Dp[i] = mx + lst[i]

print(max(Dp))

