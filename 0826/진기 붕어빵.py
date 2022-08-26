import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    bb = 0
    ans = 'Possible'
    lst.sort()
    for i in range(1, N+1):
        if lst[i] < M:
            ans = 'Impossible'
            break
        bb += (lst[i]//M - lst[i-1]//M)*K
        bb -= 1
        if bb < 0:
            ans = 'Impossible'
            break

    print(f'#{test_case} {ans}')



