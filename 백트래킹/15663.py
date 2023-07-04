import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [0] * N


def solve():

    if len(ans) == M:
        print(*ans)
        return

    remember = 0
    for i in range(N):
        if visited[i] == 0 and remember != arr[i]:
            visited[i] = 1
            ans.append(arr[i])
            remember = arr[i]
            solve()
            visited[i] = 0
            ans.pop()


solve()