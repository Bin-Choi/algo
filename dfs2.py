import sys
sys.stdin =open("input.txt" , "r")

def dfs(s):
    # [1] stk 등 필요자료구조 초기화
    stk = []
    visited[s] = 1

    while True:
        for e in adjL[s]:
            if not visited[e]:
                stk.append(s)

                s = e
                visited[s] = 1
                break
        else:
            if stk:
                s = stk.pop()
            else:# stack empty
                break




T = int(input())
for test_case in range(1, T + 1):
    V ,E = map(int,input().split())
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adjL[s].append(e) # 단방향

    s, g = map(int, input().split())

    visited = [0]*(V+1)
    dfs(s)

    print(f'#{test_case} {visited[g]}')
