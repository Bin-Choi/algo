import sys
sys.stdin = open("input.txt", "r")

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

s, e = 1, arr[-1] - arr[0]
result = 0

while s <= e:
    mid = (s+e) // 2
    cur = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:
            cnt += 1
            cur = arr[i]

    if cnt >= c:
        s = mid + 1
        result = mid

    else:
        e = mid - 1

print(result)
