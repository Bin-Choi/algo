import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = 1
ans = []
for i in range(1, N+1):
    for j in range(0, i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

mx = max(dp)
print(mx)
for i in range(N, 0, -1):
    if dp[i] == mx:
        ans.append(lst[i])
        mx -= 1

ans.reverse()
for i in ans:
    print(i, end=' ')




