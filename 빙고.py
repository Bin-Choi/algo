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

    elif list(zip(*arr1))[c] == [0]*5:
        Bingo += 1

    elif l == c:
        Bingo += check_cross1(arr1)

    elif c == 4-l:
        Bingo += check_cross2(arr1)

    return Bingo


arr = [list(map(int, input().split())) for _ in range(5)]
bingo = 0
cnt = 0

nums = [0]
for i in range(5):
    nums += map(int, input().split())


while bingo < 3:
    for num in range(1, 26):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == nums[num]:
                    arr[i][j] = 0
                    cnt += 1
                    bingo += check_bingo(arr, i, j)
    print(num)



