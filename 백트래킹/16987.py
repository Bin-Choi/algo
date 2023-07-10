import sys
sys.stdin = open("input.txt", "r")


def dfs(n, cnt):
    global ans
    if ans >= (cnt+(N-n)*2): # 끝까지 진행해도 최대값이 안나옴(가지치기)
        return

    if n == N:                                  # 모든 계란을 손에 들고 부딪히기 완료
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0:                          # 현재 계란이 깨진 경우 -> 다음 계란
        dfs(n+1, cnt)
    else:                                       # 현재 계란 안깨진 상태
        flag = False                            # 한번도 안 부딪혔더라도 다음 단계로 가야됨
        for j in range(N):                      # 하나씩 부딪히기
            if n == j or arr[j][0] <= 0:
                continue
            flag = True                         # 부딪혔으면 플래그 트루
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n+1, cnt+int(arr[n][0] <= 0)+int(arr[j][0] <= 0))
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]
        if flag == False:                       # 한번도 안깨졌다(부딪힐 상대가 없다)
            dfs(n+1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 0)                      # 계란 index, 깨진 계란 개수
print(ans)

