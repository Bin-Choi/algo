import sys
from collections import deque
sys.stdin = open("input.txt", "r")

Time = int(input())
r = 0
for _ in range(Time):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    q = deque(arr)
    r = 0
    if n == 0:
        q = []

    for c in p:
        e = 0
        if c == 'R':
            if q:
                r += 1
            else:
                e = 1
        elif c == 'D':
            if q:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                e = 1
    if e == 1:
        print('error')

    else:
        if r % 2 == 0:
            print(q)
        else:
            q = q.reverse()
            print(q)