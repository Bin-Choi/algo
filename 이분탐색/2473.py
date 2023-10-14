import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = []
m = float("INF")
for i in range(n-2):
    s, e = i+1, n-1

    while s < e:
        mid = arr[s] + arr[e]
        if abs(arr[i] + mid) < abs(m):
            m = abs(arr[i] + mid)
            ans = [arr[i], arr[s], arr[e]]

        if arr[i] + mid == 0:
            ans = [arr[i], arr[s], arr[e]]
            break

        elif arr[i] + mid > 0:
            e -= 1

        else:
            s += 1

print(*ans)



