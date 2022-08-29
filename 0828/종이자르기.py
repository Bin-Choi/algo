import sys
sys.stdin = open("input.txt", "r")

W, H = map(int, input().split())
N = int(input())
w = []
h = []
for i in range(W):
    w.append(1)
    w.append(0)
for i in range(H):
    h.append(1)
    h.append(0)
mw = mh = 0
cnt = 0
for n in range(N):
    i, j = map(int, input().split())
    if i == 0:
        h[2*j] = 2
    else:
        w[2*j] = 2

for i in range(2*W):
    if w[i] == 0:
        cnt += 1
        if mw <= cnt:
            mw = cnt
    elif w[i] == 2:
        cnt = 0
cnt = 0
for j in range(2*H):
    if h[j] == 0:
        cnt += 1
        if mh <= cnt:
            mh = cnt
    elif h[j] == 2:
        cnt = 0

print(mh * mw)
