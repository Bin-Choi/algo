import sys
sys.stdin = open("input.txt", "r")


def m_sum(ij, mn, slst, blst):              #크기가 작은쪽이 slst
    sum1 = 0
    for idx in range(mn):
        sum1 += slst[idx]*blst[ij+idx]
    return sum1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    Max = -9999
    if N < M:
        for i in range(M-N+1):
            Sum = m_sum(i, N, lst1, lst2)
            if Max < Sum:
                Max = Sum

    else:
        for j in range(N-M+1):
            Sum = m_sum(j, M, lst2, lst1)
            if Max < Sum:
                Max = Sum

    print(f'#{test_case} {Max}')
