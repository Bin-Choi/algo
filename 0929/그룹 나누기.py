import sys
sys.stdin = open("input.txt", "r")


def find_set(n):
    while n != p[n]:
        n = p[n]
    return n


def union(a, b):
    p[find_set(b)] = find_set(a)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] make_set :개별 집합을 생성
    p = [n for n in range(N+1)]

    # [2] 입력받은 희망조와 합쳐줌
    for i in range(0, len(lst), 2):
        union(lst[i], lst[i+1])

    # [3] 그룹의 대표수를 카운트( n == p[n] )
    ans = 0
    for n in range(1, N+1):
        if n == p[n]:
            ans += 1

    print(f'#{test_case} {ans}')