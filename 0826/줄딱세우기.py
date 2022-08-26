import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = [0] + list(map(int, input().split()))
cnt = [0] * (N+1)
for i in range(1, N+1):
    cnt[i] = i

for i in range(1, N+1):
    if lst[i] != 0:
        for j in range(lst[i]):
            cnt[i-j-1], cnt[i-j] = cnt[i-j], cnt[i-j-1]
print(*cnt[1:])