import sys
sys.stdin = open("input.txt", "r")

lst = [0]*5
cnt = [0]*5

N = int(input())
for i in range(6):
    p, q = map(int, input().split())
    h1 = w1 = 0
    h2 = w2 = 500#큰거1 작은거2
    if p == 1:
        cnt[1] += 1
        if lst[1] != 0:
            w2 = lst[1]
            lst[1] = q
        else:
            lst[1] = q
    elif p == 2:
        cnt[2] += 1
        if lst[2] != 0:
            w2 = lst[2]
            lst[2] = q
        else:
            lst[2] = q
    elif p == 3:
        cnt += 1
        if lst[3] != 0:
            h2 = lst[3]
            lst[3] = q
        else:
            lst[3] = q
    else:
        cnt += 1
        if lst[4] != 0:
            h2 = lst[4]
            lst[4] = q
        else:
            lst[4] = q

if cnt[1] == 1:
    w1 = lst[1]
else:
    w1 = lst[2]

if cnt[3] == 1:
    h1 = lst[3]
else:
    h1 = lst[4]


lend = (h1*w1)-(h2*w2)
print(N * lend)

