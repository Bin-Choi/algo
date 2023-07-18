import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}
for i in arr:
    tem = i
    if tem in dic:
        dic[tem] += 1
    else:
        dic[tem] = 1

dic = sorted(dic.items(), key = lambda x: -x[1])

for i in dic:
    for j in range(i[1]):
        print(i[0], end=' ')