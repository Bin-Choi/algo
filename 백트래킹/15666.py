import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []


def solve(last):
    if len(ans) == M:
        print(*ans)
        return

    remember = 0
    for i in range(last, N):
        if not remember == arr[i]:
            remember = arr[i]
            ans.append(arr[i])
            solve(i)
            ans.pop()


solve(0)