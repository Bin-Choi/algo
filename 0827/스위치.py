import sys
sys.stdin = open("input.txt", "r")


def change(idx):
    if switch[idx] == 1:
        switch[idx] = 0
    elif switch[idx] == 0:
        switch[idx] = 1


N = int(input())
switch = [5]+list(map(int, input().split()))
M = int(input())
for n in range(M):
    t, s = map(int, input().split())
    if t == 1:
        for i in range(1, N+1):
            if i % s == 0:
                change(i)
    else:
        l = 0
        for j in range(1, N//2):
            if switch[s-j:s+j+1] == switch[s-j:s+j+1][::-1]:
                l = j
            else:
                break

        if l == 0:
            change(s)
        else:
            for u in range(s-l, s+l+1):
                change(u)
switch = switch[1:]

for x in range(0, N, 20):
    print(*switch[x:x+20])