import sys
sys.stdin = open("input.txt", "r")

A = list(map(int, input().split()))
B = [1, 2, 3, 4, 5]

cnt = 0

while A != B:
    i = cnt % 4
    if A[i] > A[i+1]:
        A[i], A[i+1] = A[i+1], A[i]
        cnt += 1
        print(*A)
    else:
        cnt += 1
