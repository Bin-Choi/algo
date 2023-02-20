import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())

lst = deque()
for i in range(1, N+1):
    lst.append(i)
ans = []

while lst:
    for _ in range(K-1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())

print(str(ans).replace('[', '<').replace(']', '>'))




