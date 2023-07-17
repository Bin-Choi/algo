import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())

    arr.append((x, y))

arr.sort()

for i in arr:
    print(i[0], i[1])