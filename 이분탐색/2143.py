import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
a = int(input())
listA = list(map(int, input().split()))
b = int(input())
listB = list(map(int, input().split()))

dictA = defaultdict(int)
ans = 0

for i in range(a):
    for j in range(i, a):
        dictA[sum(listA[i:j+1])] += 1

for i in range(b):
    for j in range(i, b):
        ans += (dictA[T - sum(listB[i:j+1])])

print(ans)