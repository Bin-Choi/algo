import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    tc = lst.pop(0)
    cnt = 0
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[i] < lst[i-j]:
                for c in range(j):
                    lst[i-1], lst[i] = lst[i], lst[i-1]
                    i = i-1
                cnt += j
                break
    print(tc, cnt)