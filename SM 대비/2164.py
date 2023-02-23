import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

q = deque()

for i in range(n):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())



