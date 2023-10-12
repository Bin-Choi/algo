import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 1
end = int(1e9)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for l in lst:
        if l >= mid:
            cnt += (l-mid)

    if cnt >= m:
        result = max(result, mid)
        start = mid+1
    else:
        end = mid-1

print(result)
