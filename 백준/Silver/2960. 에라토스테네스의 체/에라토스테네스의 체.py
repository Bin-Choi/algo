def gggg():
    k = 0
    while True:
        for i in range(len(stk)):
            if stk[i] != 0:
                m = stk[i]
                for j in range(len(stk)):
                    if stk[j] % m == 0 and stk[j] != 0:
                        ans = stk[j]
                        stk[j] = 0
                        k += 1
                        if k == K:
                            return ans


N, K = map(int, input().split())
k = 0
stk = []
for i in range(2, N+1):
    stk.append(i)
ans = gggg()
print(ans)