import bisect
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
aa = []
bb = []
cc = []
dd = []
ab = []
cd = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    aa.append(a)
    bb.append(b)
    cc.append(c)
    dd.append(d)

for i in range(n):
    for j in range(n):
        ab.append(aa[i] + bb[j])
        cd.append(cc[i] + dd[j])

ab.sort()
cd.sort()

left, right = 0, len(cd)-1
res = 0

while left < len(ab) and right >= 0:
    tmp = ab[left] + cd[right]
    cs, ce = left + 1, right - 1

    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        ab_left, ab_right = bisect.bisect_left(ab, ab[left]), bisect.bisect_right(ab, ab[left])
        cd_left, cd_right = bisect.bisect_left(cd, cd[right]), bisect.bisect_right(cd, cd[right])
        res += (ab_right-ab_left) * (cd_right-cd_left)
        left = ab_right
        right = cd_left-1

print(res)





