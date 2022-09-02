import sys
sys.stdin = open("input.txt", "r")
a, b, c, m = map(int, input().split())
h = g = w = 0
while h != 24:
    h += 1
    if a > m:
        break
    if g + a <= m:
        g += a
        w += b
    else:
        if g - c >= 0:
            g -= c
        else:
            g = 0

print(w)