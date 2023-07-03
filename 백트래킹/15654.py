import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()


def dfs(ans):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        if not arr[i] in ans:
            ans.append(arr[i])
            dfs(ans)
            ans.pop()


dfs(ans)


