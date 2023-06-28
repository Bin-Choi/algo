import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]


def dev(n, r, c):

    global ans
    if n == 1:
        ans[arr[r][c]] += 1
        return

    flag = 0

    for i in range(n):
        for j in range(n):
            if arr[r][c] != arr[r+i][c+j]:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 0:
        ans[arr[r][c]] += 1
        return

    elif flag == 1:
        # 4분할s
        n = n//2
        for i in range(2):
            for j in range(2):
                dev(n, r+(n*i), c+(n*j))


dev(n, 0, 0)
for i in range(2):
    print(ans[i])