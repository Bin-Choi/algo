import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def solve():
    for leng in range(N, 1, -1):
        for lst in arr1:
            for i in range(N-leng+1): #시작위치
                if lst[i:i+leng] == lst[i:i+leng][::-1]:
                    return leng

        for lst in arr2:
            for i in range(N-leng+1):  # 시작위치
                if lst[i:i + leng] == lst[i:i + leng][::-1]:
                    return leng
    return leng


for test_case in range(1, T+1):
    N = 100
    arr1 = [input() for _ in range(N)]
    arr2 = list(zip(*arr1))

    ans = solve()

    print(f'#{test_case} {ans}')

