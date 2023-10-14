import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
cnt = 0

for i in range(n):
    s, e = 0, n-1
    while s < e:
        mid = arr[s] + arr[e]
        if mid == arr[i]:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                cnt += 1
                break
        elif mid > arr[i]:
            s += 1
        else:
            e -= 1
print(cnt)