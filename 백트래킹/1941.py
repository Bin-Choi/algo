import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(si, sj):
    q = deque()
    v2 = [[0]*5 for _ in range(5)]

    q.append((si, sj))
    v2[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v2[ni][nj] == 0 and v1[ni][nj] == 1:
                q.append((ni, nj))
                v2[ni][nj] = 1
                cnt += 1
    return cnt == 7


def check():
    for i in range(5):
        for j in range(5):
            if v1[i][j] == 1:
                return bfs(i, j)


def dfs(n, cnt, s_cnt):
    global ans
    if cnt > 7:                         # 가지치기
        return

    if n == 25:
        if cnt == 7 and s_cnt >= 4:     # 7명 그룹이고, 4명 이상이 다솜파인 경우(정답 체크)
            if check():                 # 인접했는지 체크해서 모두 인접시 정답 += 1
                ans += 1
        return

    v1[n//5][n%5] = 1                    # 포함
    dfs(n+1, cnt+1, s_cnt+int(arr[n//5][n%5] == 'S'))
    v1[n//5][n%5] = 0                    # 원상복구
    dfs(n+1, cnt, s_cnt)                # 비포함


arr = [input() for _ in range(5)]
ans = 0
v1 = [[0]*5 for _ in range(5)]
# 학생번호(0~24), 포함학생수, 다솜파학생수
dfs(0,0,0)
print(ans)
