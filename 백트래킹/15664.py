import sys
sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [0] * N


def solve(start):
    if len(ans) == M:
        print(*ans)
        return

    last = 0
    for i in range(start, N):
        if not visited[i] and last != arr[i]:
            visited[i] = 1
            ans.append(arr[i])
            last = arr[i]
            solve(i+1)
            visited[i] = 0
            ans.pop()


solve(0)
