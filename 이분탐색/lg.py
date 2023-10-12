import sys

sys.stdin = open("input.txt", "r")
N = 5
dist = [list(map(int, input().split())) for _ in range(N)]
d = [0] * N
# 부호
dp = [1] * N
d[1] = dist[1][0]

for i in range(2, N):
        # 점 i는 점 i-1과 부호가 다름
    if dist[i][0] + dist[i-1][0] == dist[i][i-1]:
        dp[i] = dp[i-1]*(-1)
        d[i] = dist[i][0]*dp[i]
    #     점 i와 점 i-1의 부호가 같음
    else:
        d[i] = dist[i][0] * dp[i-1]

answer = sorted(range(len(d)), key=lambda x: d[x])
print(answer)
print(answer[::-1])


# 0 2 3 1
# 2 0 1 1
# 3 1 0 2
# 1 1 2 0

