import sys
sys.stdin = open("input.txt", "r")

N = input()
n = [0]*9

for i in N:
    if i == '0':
        n[0] += 1
    elif i == '1':
        n[1] += 1
    elif i == '2':
        n[2] += 1
    elif i == '3':
        n[3] += 1
    elif i == '4':
        n[4] += 1
    elif i == '5':
        n[5] += 1
    elif i == '6' or i == '9':
        n[6] += 1
    elif i == '7':
        n[7] += 1
    elif i == '8':
        n[8] += 1

if n[6] % 2:
    n[6] = n[6]//2 + 1
else:
    n[6] = n[6]//2

print(max(n))

