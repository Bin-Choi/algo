import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, P = map(int, input().split())
    lst = [N//P]*P

    for i in range(N % P):
        lst[i] += 1

    ans = 1
    for n in lst:
        ans *= n
    print(f'#{test_case} {ans}')
