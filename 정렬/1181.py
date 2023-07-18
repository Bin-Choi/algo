import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(input())


arr = sorted(set(arr), key = lambda x: (len(x), x))

for i in arr:
    print(i)