import sys
from collections import deque
sys.stdin = open("input.txt", "r")

Time = int(input())
for _ in range(Time):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    q = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if '' in q:
        q.pop()

    r = 0
    e = 0

    for cmd in p:
        if cmd == "R":
            r += 1
        else:
            if len(q) < 1:
                e = 1
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if e == 1:
        print('error')
    else:
        if r % 2 == 0:
            print("["+",".join(q)+"]")
        else:
            q.reverse()
            print("["+",".join(q)+"]")