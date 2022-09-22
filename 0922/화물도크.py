import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    tt = [list(map(int, input().split())) for _ in range(N)]
    tt = sorted(tt, key=lambda x: x[1])
    i = 0
    l = len(tt)
    ans = 0
    end = 0
    while i < l:
        if tt[i][0] >= end:
            ans += 1
            end = tt[i][1]
        i += 1
    print(f'#{test_case} {ans}')