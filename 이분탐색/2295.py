import sys
import bisect
sys.stdin = open("input.txt", "r")


def cnt_bisect(arr, target):
    r_idx = bisect.bisect_right(arr, target)
    l_idx = bisect.bisect_left(arr, target)
    return r_idx-l_idx


n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
a.sort()
two = []
for i in range(n):
    for j in range(i, n):
        two.append(a[i]+a[j])

two = sorted(set(two))
flag = 0
for i in range(n-1, -1, -1):
    if flag == 1:
        break
    for j in range(i+1):
        if cnt_bisect(two, a[i]-a[j]):
            print(a[i])
            flag = 1
            break

