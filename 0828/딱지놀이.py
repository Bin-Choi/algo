import sys
sys.stdin = open("input.txt", "r")


def winner(A, B):
    while A:
        a = A.pop()
        b = B.pop()
        if a > b:
            return "A"
        elif a < b:
            return "B"
    return "D"


Round = int(input())
for r in range(Round):
    rA = list(map(int, input().split()))
    rB = list(map(int, input().split()))
    A = [0] * 5
    B = [0] * 5
    rA.pop(0)
    rB.pop(0)

    for i in range(len(rA)):
        ai = rA[i]
        A[ai] += 1
    for j in range(len(rB)):
        bi = rB[j]
        B[bi] += 1

    print(winner(A, B))