import math
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
for n in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    c1 = abs(x2-x1)
    c2 = abs(y2-y1)
    d = math.sqrt((c1*c1)+(c2*c2))
    ans = 2
    d1 = math.isclose(d, r1+r2)
    d2 = math.isclose(d, abs(r1-r2))
    if c1 == 0 and c2 == 0:
        if r1 == r2:
            ans = -1
        else:
            ans = 0
    else:
        if d1 is True or d2 is True:
            ans = 1

        if d > r1+r2:
            ans = 0

        if d < abs(r1-r2):
            ans = 0

    print(ans)

