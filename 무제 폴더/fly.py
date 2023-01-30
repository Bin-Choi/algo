import sys
sys.stdin =open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2*(M-1)) for _ in range(M-1)]+[[0]*(M-1)+list(map(int,input().split()))+[0]*(M-1) for _ in range(N)] + [[0]*(N+2*(M-1)) for _ in range(M-1)]

    i = j = 0
    max = 0

    for i in range(M-1, N+M-1):
        for j in range(M-1, N+M-1):
            p = c = 0
            k = 1
            while k < M:
                p += arr[i-k][j] + arr[i+k][j] + arr[i][j-k] + arr[i][j+k]
                c += arr[i-k][j-k] + arr[i-k][j+k] + arr[i+k][j-k] + arr[i+k][j+k]
                k += 1
            if p + arr[i][j] > c + arr[i][j]:
                sum = p + arr[i][j]
            else:
                sum = c + arr[i][j]

            if sum > max:
                max = sum

    print(f'#{test_case} {max}')
#                     교 수 님 풀 이
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     for si in range(N): # + 모양
#         for sj in range(N): # 기준좌표 si,sj
#
#             cnt = arr[si][sj]
#             for mul in range(1, M):
#                 for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#                     ni, nj = si + di * mul, sj + dj * mul
#                     if 0 <= ni < N and 0 <= nj < N:
#                         cnt += arr[ni][nj]
#             if ans < cnt:
#                 ans = cnt
#     for si in range(N):  # X 모양
#         for sj in range(N):  # 기준좌표 si, sj
#
#             cnt = arr[si][sj]
#             for mul in range(1, M):
#                 for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
#                     ni, nj = si + di * mul, sj + dj * mul
#                     if 0 <= ni < N and 0 <= nj < N:
#                         cnt += arr[ni][nj]
#             if ans < cnt:
#                 ans = cnt
#
#     print(f'#{test_case} {ans}')
