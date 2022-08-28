import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def is_same(arr, n, m):

    for _ in range(2):
        for i in arr:
            for j in range(n-m+1):
                if i[j:j+m] == i[j:j+m][::-1]:
                    return i[j:j+m]
        arr = list(map(list, zip(*arr)))






for test_case in range(1, T+1):

    N, M = map(int, input().split())
    Arr = [list(input()) for _ in range(N)]
    ans = is_same(Arr, N, M)

    print(f'#{test_case} {"".join(ans)}')




