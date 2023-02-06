# N과 M
import sys
sys.stdin = open("input.txt", "r")

N, M = list(map(int, input().split()))

s = []

# N = 4 , M = 3 이라고 놓고 푼다?
def dfs():
    if len(s) == 3:
        print(' '.join(map(str, s)))
        return

    for i in range(1, 4+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
