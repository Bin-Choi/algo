import sys
sys.stdin = open("input.txt", "r")

arr = [[0] * 1001 for _ in range(1001)]
N = int(input())
cnt = [0] * (N+1)
for n in range(1,N+1):
    si, sj, h, w = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n

for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            n = arr[i][j]
            cnt[n] += 1

cnt.pop(0)
for p in range(N):
    print(cnt[p])
