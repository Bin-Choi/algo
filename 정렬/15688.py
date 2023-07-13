import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr1 = [0] * 1000001
arr2 = [0] * 1000001
for i in range(N):
    a = int(input())
    if a >= 0:
        arr1[a] += 1
    else:
        arr2[-a] += 1

for i in range(1000000, 0, -1):
    if arr2[i] != 0:
        for j in range(arr2[i]):
            print(-i)


for i in range(1000001):
    if arr1[i] != 0:
        for j in range(arr1[i]):
            print(i)
