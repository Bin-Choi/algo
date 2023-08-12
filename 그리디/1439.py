import sys
sys.stdin = open("input.txt", "r")

S = list(map(int, input()))

s = S[0]
cnt = [0]*2

cnt[s] += 1
for i in range(1, len(S)):
    if s != S[i]:
        s = S[i]
        cnt[s] += 1

print(min(cnt))




