import sys
sys.stdin = open("input.txt", "r")

N = int(input())
nums = list(map(int, input().split()))
m = int(input())

s, e = 0, max(nums)
ans = 0

while s <= e:
    total = 0
    mid = (s+e) // 2

    for num in nums:
        total += min(mid, num)

    if total <= m:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)

