import sys
sys.stdin = open("input.txt", "r")

A = []
B = []
C = []
D = []
E = []
F = []
af = bd = ce = m = max = 0
N = int(input())
for n in range(N):
    a, b, c, d, e, f = map(int, input().split())
    A.append(a)
    af += (a+f)
    B.append(b)
    bd += (b+d)
    C.append(c)
    ce += (c+e)
    E.append(e)
    D.append(d)
    F.append(f)

if af < bd:
    m = af
    if af > ce:
        m = ce
else:
    if bd < ce:
        m = bd

if m == af:
    for i in range(N):
        if B[i] < CE[i]:
            max += CE[i]
        else:
            max += BD[i]
elif m == bd:
    for i in range(N):
        if AF[i] < CE[i]:
            max += CE[i]
        else:
            max += AF[i]
else:
    for i in range(N):
        if AF[i] < BD[i]



