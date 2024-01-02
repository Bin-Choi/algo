import sys
sys.stdin = open("input.txt", "r")

N, S = map(int, input().split())
arr = list(map(int, input().split()))
s = arr[0]
result = int(2e9)

left, right = 0, 0

while True:
    if s >= S:
        s -= arr[left]
        result = min(result, right - left + 1)
        left += 1
    else:
        right += 1
        if right == N:
            break
        s += arr[right]

if result == int(2e9):
    print(0)
else:
    print(result)


