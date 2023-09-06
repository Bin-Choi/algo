import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
arr = sorted(set(num))

dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i

for i in num:
    print(dic[i], end=" ")
