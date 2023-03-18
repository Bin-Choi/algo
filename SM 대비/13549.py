import sys
from collections import deque
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
road = [0] * 100001

q = deque()
q.append(N)
road[N] = 1
while q:
    x = q.popleft()
    if x == K:
        print(road[x]-1)
        break
    for nx in (2*x, x-1, x+1):
        if 100001 > nx >= 0 == road[nx]:
            if nx == 2*x:
                road[nx] = road[x]
                q.appendleft(nx)
            else:
                road[nx] = road[x] + 1
                q.append(nx)