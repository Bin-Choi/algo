N, M = map(int, input().split())
s = []


def dfs(i):
    if len(s) == M:
        print(*s)
        return

    for i in range(i, N+1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)
