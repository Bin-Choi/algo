import sys
from collections import deque
sys.stdin = open("input.txt", "r")

Max = 100001
n, k = map(int, input().split())
arr = [0] * Max


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()

        if v == k:
            return arr[v]

        for nv in (v-1, v+1, v*2):
            if 0 <= nv < Max and not arr[nv]:
                arr[nv] = arr[v] + 1
                q.append(nv)

print(bfs(n))