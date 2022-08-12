import sys
sys.stdin =open("input.txt" , "r")

T = int(input())

for test_case in range(1, T+1):
    BS = [0] * 501
    N = int(input())
    for n in range(1, N+1):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            BS[i] += 1
    p = int(input())

    print(f'#{test_case}', *BS[1:p+1])
