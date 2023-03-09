import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(s, g):
    q = deque()
    q.append(s)

    while q:
        k = q.popleft()
        if k == g:
            return tower[k]-1
        for i in range(2):
            nk = k + dk[i]
            if 0 < nk <= f and tower[nk] == 0:
                tower[nk] = tower[k] + 1
                q.append(nk)

    return "use the stairs"


f, s, g, u, d = map(int, input().split())

tower = [0] * (f+1)
ans = 0
dk = [u, -d]
tower[s] = 1
ans = bfs(s, g)
print(ans)
