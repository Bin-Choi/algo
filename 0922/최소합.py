def dfs(ci, cj, sm):
    global ans
    if ans <= sm:
        return
    if ci == N and cj == N:
        ans = min(ans, sm)
        return
    if ci < N:
        dfs(ci+1, cj, sm+arr[ci+1][cj])
    if cj < N:
        dfs(ci, cj+1, sm+arr[ci][cj+1])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 위, 왼쪽에 0을 한 겹 씌움
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N * 2
    dfs(1, 1, arr[1][1])

    print(f'#{test_case} {ans}')