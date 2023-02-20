import sys
sys.stdin = open("input.txt", "r")

A = [0] * 26
B = A[:]
ans = 0

N = input()
M = input()

for n in N:
    A[ord(n)-97] += 1
for m in M:
    B[ord(m)-97] += 1

for i in range(26):
    ans += abs(A[i]-B[i])

print(ans)
