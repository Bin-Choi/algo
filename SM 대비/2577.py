import sys
sys.stdin = open("input.txt", "r")

A = int(input())
B = int(input())
C = int(input())
N = [0]*10

num = str(A * B * C)

for n in num:
    if n == '0':
        N[0] += 1
    elif n == '1':
        N[1] += 1
    elif n == '2':
        N[2] += 1
    elif n == '3':
        N[3] += 1
    elif n == '4':
        N[4] += 1
    elif n == '5':
        N[5] += 1
    elif n == '6':
        N[6] += 1
    elif n == '7':
        N[7] += 1
    elif n == '8':
        N[8] += 1
    elif n == '9':
        N[9] += 1

for cnt in N:
    print(cnt)