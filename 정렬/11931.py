import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr =[]
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
for i in range(N):
    print(arr[i])