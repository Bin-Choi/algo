import sys
sys.stdin = open("input.txt", "r")

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check_bd(y, x):  # 경계 체크
    if y < 0 or x < 0 or y >= N or x >= N:
        return True # 경계 벗어남
    return False


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    y, x = 0, 0                         # 시작좌표
    result = 0                          # 정답출력
    for i in range(N):
        if 2 in arr[i]:              # 출발점 찾기
            x = arr[i].index(2)
            y = i
            break
    stk = [(y, x)]                  # 스택에 시작점 넣기

    while stk:                      # 스택이 빌때까지
        y, x = stk.pop()            # 현재 좌표 꺼내서
        arr[y][x] = 1               # 방문처리
        for _y, _x in move:         # 이동할 방향검사
            dy = y + _y
            dx = x + _x
            if check_bd(dy, dx):    # 경계 벗어나면 다음 길
                continue
            if arr[dy][dx] == 3:    # 도착
                result = 1
                break
            elif not arr[dy][dx]:   # 통로 만나면 스택에 추가
                stk.append((dy, dx))
        else:
            continue
        break


# def is_safe(y, x):
#     return 0 <= y < N and 0 <= x < N and (arr[y][x] == 0 or arr[y][x] == 3)
#
#
# def DFS(sy, sx):
#     global result
#
#     if arr[sy][sx] == 3:
#         result = 1
#         return
#
#     visited.append((sy, sx))
#     for dj in range(4):
#         go_y = sy + dy[dj]
#         go_x = sx + dx[dj]
#         if is_safe(go_y, go_x) and (go_y, go_x) not in visited:
#             DFS(go_y, go_x)
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         if 2 in arr[i]:  # 출발점 찾기
#             s_y, s_x = i, arr[i].index(2)
#
#     dy = [-1, 1, 0, 0]
#     dx = [0, 0, -1, 1]
#
#     visited = []
#     result = 0
#     DFS(s_y, s_x)
    print(f'#{test_case} {result}')