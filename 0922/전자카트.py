import sys
sys.stdin = open('input.txt', 'r')


def BFS(cur, start, total):
    global min_total
    if total > min_total:
        return
    if cur == N-1:
        min_total = min(min_total, arr[start][0]+total)
        return

    for i in range(1, N):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            BFS(cur+1, i, total+arr[start][i])
            visited[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    min_total = 1001
    BFS(0, 0, 0)

    print(f'#{test_case} {min_total}')

