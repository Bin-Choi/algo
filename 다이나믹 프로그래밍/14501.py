import sys
sys.stdin = open("input.txt", "r")

n = int(input())
d = [0] * (n+1)
T = [0] * (n+1)
P = [0] * (n+1)
d[1] = P[1]

for i in range(1, n+1):
    t, p = map(int, input().split())
    T[i] = t + i - 1
    P[i] = p

for i in range(1, n+1):
    mx = 0
    for j in range(0, i):
        if i > T[j]:
            mx = max(mx, d[j])
    if T[i] < n+1:
        d[i] = mx + P[i]

print(max(d))





