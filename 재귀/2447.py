import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [[ " " for i in range(n)] for j in range(n)]


def star(n, r, c):

    # 별 찍기
    if n == 1:
        arr[r][c] = '*'
        return

    # 9분할 하기
    n = n//3
    for i in range(3):
        for j in range(3):
            # 가운데 ( i, j = 1 ) 빼고 다시 쪼개기
            if i == 1 and j == 1:
                pass
            else:
                star(n, r+(n * i), c+(n*j))


star(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(*arr[i][j], end='')
    print()
