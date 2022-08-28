import sys
sys.stdin = open("input.txt", "r")


w, h = map(int, input().split())
dr = [1, -1]
d1 = d2 = 0
m1 = m2 = 1
si, sj = map(int, input().split())
H = int(input())
H1 = H % (2*w)
H2 = H % (2*h)
while m1 <= H1:
    fi = si + dr[d1]
    if 0 <= fi <= w:
        si = fi
        m1 += 1
    else:
        d1 = (d1 + 1) % 2
while m2 <= H2:
    fj = sj + dr[d2]
    if 0 <= fj <= h:
        sj = fj
        m2 += 1
    else:
        d2 = (d2 + 1) % 2

print(si, sj)


