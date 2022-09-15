import sys
sys.stdin = open("input.txt", "r")


def inord(n):
    global cnt
    if n:
        cnt += 1
        inord(ch1[n])
        inord(ch2[n])
    return


T = int(input())
for test_case in range(1, T+1):
    V, S = map(int, input().split())
    lst = list(map(int, input().split()))
    ch1 = [0] * (V+2)
    ch2 = [0] * (V+2)
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    inord(S)
    print('#{} {}'.format(test_case, cnt))

