import sys
sys.stdin = open("input.txt", "r")

k, n = map(int, sys.stdin.readline().rstrip().split())
line = []

for _ in range(k):
    line.append(int(sys.stdin.readline().rstrip()))

line.sort()
start = 1
end = max(line)
result = 0


while(start <= end):
    cnt = 0
    mid = (start + end) // 2

    for x in line:
        if x >= mid:
            cnt += (x // mid)

    if cnt < n:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)


