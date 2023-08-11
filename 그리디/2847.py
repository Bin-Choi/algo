import sys

sys.stdin = open("input.txt", "r")

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

mx = lst[-1]
cnt = 0

for i in range(n - 2, -1, -1):
    if mx <= lst[i]:
        cnt += (lst[i] - mx + 1)
        lst[i] = mx - 1
    mx = lst[i]

print(cnt)
