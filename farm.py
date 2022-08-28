import sys
sys.stdin =open("input.txt" , "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    m = N // 2

    for i in range(m):

        ans += arr[i][m]
        for j in range(1, i+1):
            ans += arr[i][m-j] + arr[i][m+j]


    for i in range(m, N):           # 가운데 ~ 끝까지 행 합
        for j in range(N):
            ans += arr[i][j]

    for i in range(1, m+1):              # 아래 빼주기
        for j in range(i):
            ans -= arr[m+i][j] + arr[m+i][N-1-j]

    print(f'#{test_case} {ans}')