import sys

sys.stdin = open("input.txt", "r")

T = int(input())

Switch = {'0': [1, 1, 1, 0, 1, 1, 1], '1': [0, 0, 1, 0, 0, 1, 0], '2': [1, 0, 1, 1, 1, 0, 1],
          '3': [1, 0, 1, 1, 0, 1, 1], '4': [0, 1, 1, 1, 0, 1, 0], '5': [1, 1, 0, 1, 0, 1, 1],
          '6': [1, 1, 0, 1, 1, 1, 1], '7': [1, 1, 1, 0, 0, 1, 0], '8': [1, 1, 1, 1, 1, 1, 1], '9': [1, 1, 1, 1, 0, 1, 1], 'Z': [0, 0, 0, 0, 0, 0, 0], }

cnt = 0
for t in range(T):
    A, B = map(str, input().split())

    while len(A) < 5:
        A = 'Z' + A
    while len(B) < 5:
        B = 'Z' + B

    for i in range(5):
        for j in range(7):
            if Switch[A[i]][j] != Switch[B[i]][j]:
                cnt += 1
    print(A, B)
    print(cnt)