import sys
sys.stdin = open("input.txt", "r")


def inord(n):
    if n <= N:
        inord(n*2)
        ans.append(lst[n])
        inord(n*2+1)

A = ['+', '-', '*', '/']


T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = [0]*(N+1)
    for i in range(1,N+1):
        lst1 = list(map(str, input().split()))
        lst[i] = lst1[1]

    ans = []
    ANS = 0
    inord(1)
    while ans:
        a = ans.pop(0)
        if a not in A:
            ANS += int(a)

        if a == '+':
            ANS += int(ans.pop(0))

        if a == '-':
            ANS -= int(ans.pop(0))

        if a == '*':
            ANS *= int(ans.pop(0))

        if a == '/':
            ANS /= int(ans.pop(0))

    print(f'#{test_case} {ANS}')





    # print(f'#{test_case} {"".join(ans)}')