import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
s = []


def dfs(s):

    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(s, N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


dfs(1)

