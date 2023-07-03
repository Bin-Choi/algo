import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()


def dfs(d):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        if arr[i] not in ans:
            if len(ans) == 0 or (arr[i] >= ans[-1]):
                ans.append(arr[i])
                dfs(d+1)
                ans.pop()


dfs(0)