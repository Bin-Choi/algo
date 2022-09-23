import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)


def DFS(start, tree, parent):
    for t in tree[start]:
        if parent[t] == 0:
            parent[t] = start
            DFS(t, tree, parent)


N = int(input())

Tree = [[] for _ in range(N+1)]
Parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

DFS(1, Tree, Parents)

for i in range(2, N+1):
    print(Parents[i])