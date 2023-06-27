import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]


def sol(N, r, c):
    global ans

    if N == 1:
        ans[arr[r][c]] += 1
        return

    flag = 0

    for i in range(N):
        for j in range(N):
            if arr[r][c] != arr[r+i][c+j]:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 0:
        ans[arr[r][c]] += 1
        return

    # 9분할
    elif flag == 1:
        N = N // 3
        for i in range(3):
            for j in range(3):
                sol(N, r+(N*i), c+(N*j))


sol(n, 0, 0)

answer = [0, 0, 0]
answer[0] = ans[2]
answer[1] = ans[0]
answer[2] = ans[1]

for i in range(3):
    print(answer[i])