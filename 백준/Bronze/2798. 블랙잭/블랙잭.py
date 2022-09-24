N, M = map(int, input().split())
Cards = list(map(int, input().split()))
ans = a1 = a2 = a3 = 0

for i in range(0, N-2):
    a1 = Cards[i]
    for j in range(i+1, N-1):
        a2 = Cards[j]
        for l in range(j+1, N):
            a3 = Cards[l]

            if a1 + a2 + a3 <= M:
                if a1 + a2 + a3 > ans:
                    ans = a1 + a2 + a3


print(ans)