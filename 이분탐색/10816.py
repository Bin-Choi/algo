import sys
sys.stdin = open("input.txt", "r")

n = int(input())
lst_a = list(map(int, input().split()))
m = int(input())
lst_b = list(map(int, input().split()))

cnt = {}
for i in lst_a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst_b:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')

