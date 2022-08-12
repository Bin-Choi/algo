import sys
sys.stdin =open("input.txt" , "r")

T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    sols = [0]*(N+1)

    for q in range(1, Q+1):
        S, E = map(int, input().split())
        for j in range(S, E+1):
            sols[j] = q
    print(f'#{test_case}', *sols[1:])