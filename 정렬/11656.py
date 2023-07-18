import sys
sys.stdin = open("input.txt", "r")

S = input()
arr = [S]

for i in range(len(S)):
    arr.append(S[i:])

arr.sort()
for i in arr:
    print(i)
