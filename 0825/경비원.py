import sys
sys.stdin = open("input.txt", "r")


def change(i, j):
    if i == 1:
        a = j
    elif i == 2:
        a = (2*N + M) - j
    elif i == 3:
        a = (2*N + 2*M) - j
    else:
        a = N + j
    return a


def check_min(market, dg):
    if abs(market-dg) < ran - abs(market-dg):
        return abs(market-dg)
    else:
        return ran - abs(market-dg)


N, M = map(int, input().split())
ran = 2*N + 2*M
n = int(input())
markets = []
ans = int(0)

for _ in range(n):
    i, j = map(int, input().split())
    markets.append(change(i, j))
si, sj = map(int, input().split())
dg = change(si, sj)
for market in markets:
    ans += check_min(market, dg)

print(ans)



