import sys
sys.stdin = open("input.txt", "r")

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for test_case in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    result = set()
    stack = []

    for i in range(4):
        for j in range(4):
            stack.append((i, j, 0, arr[i][j]))
            while stack:
                y, x, count, ans = stack.pop()
                if count >= 6:
                    result.add(ans)
                    continue
                for d in dr:
                    ny = y + d[0]
                    nx = x + d[1]
                    if 0 <= ny < 4 and 0 <= nx < 4:
                        stack.append((ny, nx, count+1, ans+arr[ny][nx]))

    print(f'#{test_case} {len(result)}')

