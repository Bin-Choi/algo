import sys
sys.stdin = open("input.txt", "r")

N, S = map(int, input().split())

lis = list(map(int, input().split()))
cnt = 0
ans = []


def solve(start):
    global cnt

    if sum(ans) == S and len(ans) > 0:
        cnt += 1

    for i in range(start, N):
        ans.append(lis[i])
        solve(i+1)
        ans.pop()


solve(0)
print(cnt)
