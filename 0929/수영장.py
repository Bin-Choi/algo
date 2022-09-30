import sys
sys.stdin = open("input.txt", "r")


def dfs(month, pay):
    global mn
    if month >= 13:
        mn = min(mn, pay)
        return
    else:
        dfs(month+1, pay+cost[0]*M[month])
        dfs(month+1, pay+cost[1])
        dfs(month+3, pay+cost[2])


T = int(input())
for test_case in range(1, T+1):
    cost = list(map(int, input().split()))
    M = [0]+list(map(int, input().split()))
    mn = cost[3]
    dfs(1, 0)

    print(f'#{test_case} {mn}')
