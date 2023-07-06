import sys
sys.stdin = open("input.txt", "r")

arr = [list(map(str, input())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0


def solve(arr, cnt_x, cnt_y):

    if cnt_y > 3:
        return

    if cnt_x + cnt_y == 3:
        arr.sort()
        return

    for i in range(5):
        for j in range(5):



            if 0<= x+i < 25 and 0<= y+j < 25 and visited[x+i][y+j] is not:
                visited[i][j] = 1
                if arr[i][j] == 'S':
                    cnt_x += 1
                else:
                    cnt_y += 1

