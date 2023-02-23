import sys
sys.stdin = open("input.txt", "r")

n = int(input())
A = list(map(int, input().split()))

num = [-1] * n
stack = []

for i in range(n):
    while stack and stack[-1][0] < A[i]:
        tmp, idx = stack.pop()
        num[idx] = A[i]
    stack.append([A[i], i])

print(*num)
