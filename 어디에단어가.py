import sys
sys.stdin = open("input.txt", "r")


def pz(arr1, n, k):
    cnt = 0
    for i in range(2):
        for lst in arr1:
            stk = []
            for j in range(n+1):
                if lst[j] == 1:
                    stk.append(lst[j])
                else:
                    if len(stk) == k:
                        cnt += 1
                        stk = []
                    else:
                        stk = []

        arr1 = list(map(list, zip(*arr1)))
    return cnt


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    ans = pz(arr, N, K)

    print(f'#{test_case} {ans}')