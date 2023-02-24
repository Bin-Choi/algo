import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, l = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
q = deque()

for i in range(n):
    while q and q[-1][0] > arr[i]:
        q.pop()

    while q and q[0][1] < i - l + 1:
        q.popleft()
    q.append((arr[i], i))
    print(q[0][0], end=' ')

