import sys
sys.stdin = open("input.txt", "r")

line = int(input())

arr = [[' '] * 2*line for _ in range(line)]


def star(n, r, c):

    # 작은 삼각형 일때, 삼각형 그리기
    if n == 3:
        arr[r][c] = '*'
        arr[r+1][c-1] = arr[r+1][c+1] = '*'
        for i in range(-2, 3):
            arr[r+2][c+i] = '*'
        return

    # 분할하기
    m = n//2
    star(m, r, c)
    star(m, r+m, c-m)
    star(m, r+m, c+m)


star(line, 0, line-1)

for i in range(line):
    print("".join(arr[i]))
