import sys
sys.stdin = open("input.txt", "r")


N = int(input())
lst = list(map(int, input().split()))
cnt1 = cnt2 = max = 1
for i in range(1, N):
    if lst[i] < lst[i-1]:
        cnt1 += 1
        cnt2 = 1
    elif lst[i] > lst[i-1]:
        cnt2 += 1
        cnt1 = 1
    else:
        cnt1 += 1
        cnt2 += 1
    if max < cnt1:
        max = cnt1
    if max < cnt2:
        max = cnt2
print(max)

