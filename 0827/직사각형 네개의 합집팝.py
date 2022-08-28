import sys
sys.stdin = open("input.txt", "r")

arr = [[0] * 101 for _ in range(101)]
cnt = 0
for square in range(4):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)