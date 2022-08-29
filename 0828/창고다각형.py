import sys
sys.stdin = open("input.txt", "r")

arr = [[0]*1001 for _ in range(1001)]
e = mh = ans = 0
s = 1000

N = int(input())
for n in range(N):
    num, h = map(int, input().split())
    if e < num:
        e = num
    if s > num:
        s = num
    if mh < h:
        mh = h
    for i in range(h):
        arr[i][num] = 1

for i in range(0, mh):
    cnt = 0
    val = 0
    for j in range(s, e+1):
        if arr[i][j] == 1:
            if val == 0:
                val += 1
                cnt = 0
            else:
                val += (cnt+1)
                cnt = 0
        else:
            cnt += 1
    ans += val

print(ans)
