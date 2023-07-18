import sys
input = sys.stdin.read
sys.stdin = open("input.txt", "r")

N, *arr = input().split()
for i in range(int(N)):
    arr[i] = arr[i][::-1]
arr = list(map(int, arr))

print(*sorted(arr), sep="\n")
