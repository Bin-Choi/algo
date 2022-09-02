import sys
sys.stdin = open("input.txt", "r")

N = int(input())
ans = []
if N == 2:
    a, b = map(int, input().split())
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            m = i
            break
    for j in range(1, int(m**0.5) + 1):
        if m % j == 0:
            ans.append(j)
            if (j**2) != m:
                ans.append(m//j)
else:
    a, b, c = map(int, input().split())
    for i in range(min(a, b, c), 0, -1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            m = i
            break
    for j in range(1, int(m ** 0.5) + 1):
        if m % j == 0:
            ans.append(j)
            if (j ** 2) != m:
                ans.append(m // j)
ans.sort()
for i in range(len(ans)):
    print(ans[i])

