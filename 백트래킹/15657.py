import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []


def solve(ans, last):

    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        if arr[i] >= last:
            ans.append(arr[i])
            last = arr[i]
            solve(ans, last)
            ans.pop()


solve(temp, 0)