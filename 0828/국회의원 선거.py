import sys
sys.stdin = open("input.txt", "r")


def buy(max, idx):
    ans = 0

    while cnt[0] <= max:
        if idx == 0:
            return ans
        cnt[idx] -= 1
        cnt[0] += 1
        ans += 1
        max = 0

        for i in range(N):
            if cnt[i] >= max:
                max = cnt[i]
                idx = i


N = int(input())
cnt = [0] * N
max = 0
ans = 0
flag = True
for n in range(N):
    v = int(input())
    cnt[n] = v
    if max < v:
        max = v
        idx = n

if max in cnt[1:] and max == cnt[0]:
    print(1)
elif cnt[0] == max:
    print(0)
else:
    ans = buy(max, idx)
    print(ans)



