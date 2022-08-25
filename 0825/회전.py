import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    print(f'#{test_case} {q[M % N]}')