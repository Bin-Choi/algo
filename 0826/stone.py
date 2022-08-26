import sys
sys.stdin = open("input.txt", "r")


def check_cross1(si, sj):
    for mul in range(1, 3):
        for di, dj in ((-1, -1), (1, 1)):
            ni, nj = si + di*mul, sj + dj*mul
            if ni < 0 or nj < 0 or N <= ni or N <= nj:
                return "NO"

            if arr[ni][nj] != 'o':
                return "NO"
    return "YES"


def check_cross2(si, sj):
    for mul in range(1, 3):
        for di, dj in ((-1, 1), (1, -1)):
            ni, nj = si + di*mul, sj + dj*mul
            if ni < 0 or nj < 0 or N <= ni or N <= nj:
                return "NO"

            if arr[ni][nj] != 'o':
                return "NO"
    return "YES"


def check_row(si, sj):
    for mul in range(1, 3):
        for di, dj in ((-1, 0), (1, 0)):
            ni, nj = si + di*mul, sj + dj*mul
            if ni < 0 or nj < 0 or N <= ni or N <= nj:
                return "NO"

            if arr[ni][nj] != 'o':
                return "NO"
    return "YES"


def check_col(si, sj):
    for mul in range(1, 3):
        for di, dj in ((0, 1), (0, -1)):
            ni, nj = si + di*mul, sj + dj*mul
            if ni < 0 or nj < 0 or N <= ni or N <= nj:
                return "NO"

            if arr[ni][nj] != 'o':
                return "NO"
    return "YES"


def check_five(si, sj):
    if check_row(si, sj) == "YES":
        return "YES"
    if check_col(si, sj) == "YES":
        return "YES"
    if check_cross1(si, sj) == "YES":
        return "YES"
    if check_cross2(si, sj) == "YES":
        return "YES"
    return "NO"


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = "NO"
    flag = True
    #시작점 찾기
    for i in range(N):
        if flag is False:
            break
        for j in range(N):
            if flag is False:
                break
            if arr[i][j] == 'o':
                si, sj = i, j
                ans = check_five(si, sj)
                if ans == "YES":
                    flag = False
                    break
    print(f'#{test_case} {ans}')
