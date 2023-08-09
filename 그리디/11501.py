import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for t in range(T):
    days = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    mx = 0
    for i in range(days-1, -1, -1):
        if lst[i] > mx:
            mx = lst[i]

        else:
            ans += (mx - lst[i])

    print(ans)


