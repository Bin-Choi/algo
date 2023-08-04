import sys
sys.stdin = open("input.txt", "r")

W, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]

lst.sort(reverse=True, key=lambda x: x[1])
w = W #남은 공간
ans = 0 #담은 가치
i = 0
while i < K:
    if w == 0:
        break

    if lst[i][0] <= w:
        w -= lst[i][0]
        ans += (lst[i][1] * lst[i][0])
        i += 1

    else:
        ans += (lst[i][1] * w)
        w -= w
        i += 1
print(ans)




