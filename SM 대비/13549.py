import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(a, b):
    q = deque()
    q.append(a)
    goal = b
    visited[a] = 1
    cnt = 0

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x]-1

        for nx in (2*x, x-1, x+1):
            if 0 <= nx <= 10000 and not visited[nx]:
                if nx == 2*x:
                    q.appendleft(nx)
                    visited[nx] = visited[x]
                else:
                    cnt += 1
                    q.append(nx)
                    visited[nx] = visited[x]+1


N, M = map(int, input().split())
visited = [0] * 100000
print(bfs(N, M))