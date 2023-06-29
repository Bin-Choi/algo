import sys
sys.stdin = open("input.txt", "r")


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True


def dfs(x):
    global cnt

    if x == n:
        cnt += 1

    else:
        for i in range(n):
            # 일차원 배열, for 문이 돌면서 이전 값은 지워짐, 같은 행에서 전의 결과는 영향을 안줌
            row[x] = i
            if check(x):
                dfs(x+1)


n = int(input())
cnt = 0
row = [0] * n

dfs(0)
print(cnt)

