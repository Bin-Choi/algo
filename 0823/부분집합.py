# 가능한 모든경우 (조합 & 백트레킹) n:행 번호

def dfs(n, sm):
    global ans

    if ans <= sm:  # 현재 합이 이미 ans보다 큰경우: 정답 갱신 가능성 없음
        return

    if n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n + 1, sm + arr[n][j])
            visited[j] = 0


# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N  # 열의 개수만큼 필요
    ans = 10 * N
    dfs(0, 0)  # n==0 (0행), sum=0

    print(f'#{test_case} {ans}')