import sys
sys.stdin = open("input.txt", "r")


def solve(s, e):
    # [1] 종료조건
    if s == e:
        return s

    # [2] 하부호출, 단위작업: 2등분해서 각각 승자 -> 최종승자
    a = solve(s, (s+e)//2)
    b = solve((s+e)//2+1, e)

    if lst[a]%3+1 == lst[b]:         # b가 이긴경우
        return b
    else:
        return a


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [0]+list(map(int, input().split()))
    ans = solve(1, N)           # 1~N사이의 최종 승리자의 idx 리턴

    print(f'{test_case} {ans}')

