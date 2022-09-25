N, K = map(str, input().split())
N = int(N)
cnt = 0

for h in range(N+1):
    if h < 10:
        H = '0' + str(h)
    else:
        H = str(h)
    if K in H:
        cnt += 3600
    else:
        for m in range(60):
            if m < 10:
                M = '0' + str(m)
            else:
                M = str(m)
            if K in M:
                cnt += 60
            else:
                for s in range(60):
                    if s < 10:
                        S = '0' + str(s)
                    else:
                        S = str(s)
                    if K in S:
                        cnt += 1
print(cnt)
