import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s, e = 0, n-1
answer = sys.maxsize

while s < e:
    mid = arr[s] + arr[e]

    if abs(mid) < abs(answer):
        answer = mid

    if mid == 0:
        break

    elif mid < 0:
        s += 1
    else:
        e -= 1

print(answer)