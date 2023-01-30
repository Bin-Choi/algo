import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    BS = [0] * 5001
    for i in range(1, N+1):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            BS[j] += 1
    p = int(input())
    print(f'#{test_case}', *BS[1:p+1])