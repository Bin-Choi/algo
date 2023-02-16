import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = [0]*2000001
cnt = 0
a.sort()

for i in a:
    if b[m-i] == 1:
        cnt += 1
    b[i] = 1

print(cnt)