import sys
sys.stdin = open("input.txt", "r")

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
ans = 0
for i in range(N):
    small_a = A[i]
    mx = 0
    idx = 0
    for j in range(N):
        if mx <= B[j]:
            idx = j
            mx = B[j]

    ans += (A[i]*mx)
    B[idx] = 0

print(ans)