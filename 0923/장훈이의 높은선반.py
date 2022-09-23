import sys
sys.stdin = open("input.txt", "r")


def bt(start, cnt):
    global result
    if cnt >= result:
        return
    if cnt >= B:
        result = cnt
        return
    if start == A:
        return

    bt(start+1, cnt)
    cnt += lst[start]
    bt(start+1, cnt)


T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    result = 200001

    bt(0, 0)

    print(f'#{test_case} {result-B}')
