import sys
sys.stdin = open("input.txt", "r")

#색칠하기

def stach(x, y):
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1


N = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0
for n in range(N):
    y, x = map(int, input().split())
    stach(x, y)


 for i in range(10):
     for j in range(10):
         if arr[i][j] == 1:
             cnt += 1
 print(cnt)
