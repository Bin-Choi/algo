import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [0] * 10000
for i in range(N):
    a = int(input())
    arr[a-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):         # 중복 출력
            print(i+1)
