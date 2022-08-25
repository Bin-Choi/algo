import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr1))
    print(f'#{test_case}')
    for i in range(N):
        a = ''.join(map(str, list(arr2[i][::-1])))
        b = ''.join(map(str, arr1[N-1-i][::-1]))
        c = ''.join(map(str, list(arr2[N-1-i])))
        print(f'{a} {b} {c}')