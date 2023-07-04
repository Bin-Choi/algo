import sys
sys.stdin = open("./input.txt", "r")


N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()


def solve(ans):

    if len(ans) >= M:
        print(*ans)
        return

    for i in range(N):
        ans.append(arr[i])
        solve(ans)
        ans.pop()


solve(ans)