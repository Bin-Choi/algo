import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

s = arr[0][1]
ans = 1
for i in range(1, N):
    if s <= arr[i][0]:
        ans += 1
        s = arr[i][1]

print(ans)


