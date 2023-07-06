import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
ans = []
vowels = ['a', 'e', 'i', 'o', 'u']


def check(s):
    cnt1 = 0    # 모음
    cnt2 = 0    # 자음
    for i in range(N):
        if s[i] in vowels:
            cnt1 += 1
        else:
            cnt2 += 1

    if cnt1 > 0 and cnt2 > 1:
        return True


def solve(start):
    if len(ans) == N:
        if check(ans) is True:
            print(''.join(ans))
            return

    for i in range(start, M):
        ans.append(arr[i])
        solve(i+1)
        ans.pop()


solve(0)

