import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for test in range(T):
    n = int(input())
    arr = [[0]+list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*(n+1) for _ in range(2)]

    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]
    if n == 1:
        print(max(dp[0][1], dp[0][1]))
        continue

    dp[0][2] = arr[1][1] + arr[0][2]
    dp[1][2] = arr[0][1] + arr[1][2]
    if n == 2:
        print(max(dp[0][2], dp[1][2]))
        continue

    for i in range(3, n+1):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))