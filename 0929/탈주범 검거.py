import sys
sys.stdin = open("input.txt", "r")


def move(n, p):
    global cnt



T = int(input())
dr = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
for test_case in range(1, T+1):
    N = int(input())
    mob = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(1,2001):
        move(1, 0)

    print(f'#{test_case} {cnt}')