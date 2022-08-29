import sys
sys.stdin = open("input.txt", "r")

Man = [0]*7
Wman = [0]*7
ans = 0

N, M = map(int, input().split())
for n in range(N):
    s, g = map(int, input().split())
    if s == 1:
        Man[g] += 1
    else:
        Wman[g] += 1

for i in range(1, 7):
    if Man[i] % M == 0:
        ans += Man[i] // M
    else:
        ans += Man[i] // M + 1
    if Wman[i] % M == 0:
        ans += Wman[i] // M
    else:
        ans += Wman[i] // M + 1

print(ans)