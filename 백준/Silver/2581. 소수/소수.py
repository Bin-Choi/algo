M = int(input())
N = int(input())
m = ans = 0
s = []
for i in range(M, N+1):
    if i == 1:
        continue
    if i == 2:
        m = 2
        s.append(2)
        ans = 2
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    if i % j == 0:
        continue
    s.append(i)
    ans = sum(s)
    m = s[0]
if s:
    print(ans)
    print(m)

else:
    print(-1)
