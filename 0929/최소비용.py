from collections import deque
import sys
sys.stdin = open("input.txt", "r")

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')

    distance = [[INF for _ in range(N)] for _ in range(N)]

    distance[0][0] = 0

    queue = deque()
    queue.append((0, 0))
    while queue:
        y,x = queue.popleft()
        for dy, dx in move:
            my, mx = dy+y, dx+x

            if 0<= my < N and 0<= mx < N:
                temp = 1
                if lst[my][mx] > lst[y][x]:
                    temp += lst[my][mx] - lst[y][x]

                if distance[my][mx] > distance[y][x] + temp:
                    distance[my][mx] = distance[y][x] + temp
                    queue.append((my, mx))
    print(f'#{test_case} {distance[N-1][N-1]}')