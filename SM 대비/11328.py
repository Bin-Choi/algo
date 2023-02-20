import sys
sys.stdin = open("input.txt", "r")

N = int(input())

for i in range(N):

    A, B = map(str, input().split())
    A = sorted(A)
    B = sorted(B)

    if A == B:
        print('Possible')
    else:
        print('Impossible')