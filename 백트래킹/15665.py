import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()


def solve():

    if len(ans) == M:
        print(*ans)
        return

    remember = 0

    for i in range(N):
        if not arr[i] == remember:
            ans.append(arr[i])
            remember = arr[i]
            solve()
            ans.pop()


solve()
