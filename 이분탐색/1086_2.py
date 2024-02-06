import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
S = 0
ans = int(2e9)
while True:
    if S >= M:
        ans = min(ans, e-s)
        S -= arr[s]
        s += 1
    elif e == N:
        break
               
    else:
        S += arr[e]
        e += 1

if ans == int(2e9):
    print(0)

else:
    print(ans)
