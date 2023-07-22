import sys
sys.stdin = open("input.txt", "r")

N = int(input())
d = [0] * 1000001
per = [0] * 1000001
ans = []

d[2] = 1
d[3] = 1
per[2] = 1
per[3] = 1
for i in range(4, N+1):

    d[i] = d[i-1] + 1
    per[i] = i-1

    if i % 2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
        per[i] = i//2

    if i % 3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
        per[i] = i//3


print(d[N])
i = N
while True:
    if i == 1:
        ans.append(i)
        break
    ans.append(i)
    i = per[i]

print(*ans)



