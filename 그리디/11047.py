import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
cnt = 0
i = N-1
while K > 0:
    cnt += K // coins[i]
    K = K % coins[i]
    i -= 1

print(cnt)