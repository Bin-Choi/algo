import sys
sys.stdin = open("input.txt", "r")

n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n+1)

d[1] = p[1]

if n > 1:
    for i in range(2, n+1):
        mx = 0
        for j in range(1, i//2 +1):
            mx = max(d[i-j]+d[j], mx)
        d[i] = max(mx, p[i])

print(d[n])


