import sys
sys.stdin = open("input.txt", "r")


def bin_search(n,s,e):
    cnt = 0
    while s <= e:
        m = (s+e)//2
        if m == n:
            cnt += 1
            return cnt
        elif m > n:
            e = m-1
            cnt += 1
        else:
            s = m+1
            cnt += 1


T = int(input())

for test_case in range(1, T+1):
    N, a, b = map(int,input().split())

    A = bin_search(a, 1, N)
    B = bin_search(b, 1, N)

    if A == B:
        ans = '0'
    elif A > B:
        ans = 'B'
    else:
        ans = 'A'
    print(f'#{test_case} {ans}')



