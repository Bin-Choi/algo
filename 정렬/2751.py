import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lis = []
for i in range(N):
    lis.append(int(input()))

lis.sort()

for i in range(N-1, -1, -1):
    print(lis[i])