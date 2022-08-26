import sys
sys.stdin = open("input.txt", "r")


def check_cross1(arr1):
    for x in range(5):
        if arr1[x][x] != 0:
            return 0
    return 1


def check_cross2(arr1):
    for x in range(5):
        if arr1[x][4-x] != 0:
            return 0
    return 1


def check_bingo(arr1, l, c):
    Bingo = 0

    if arr1[l] == [0]*5:
        Bingo += 1

    if list(list(zip(*arr1))[c]) == [0]*5:
        Bingo += 1

    if l == c:
        Bingo += check_cross1(arr1)

    if c == 4-l:
        Bingo += check_cross2(arr1)

    return Bingo


def check_num(arr1, num):
    for i in range(5):
        for j in range(5):
            if arr1[i][j] == num:
                arr1[i][j] == 0
                return i, j


arr = [list(map(int, input().split())) for _ in range(5)]

nums = []
for i in range(5):
    nums += map(int, input().split())

bingo = ni = nj = ans = 0


for num in nums:
    i, j = check_num(arr, num)
    arr[i][j] = 0
    bingo += check_bingo(arr, i, j)
    ans += 1
    if bingo >= 3:
        break
print(ans)

