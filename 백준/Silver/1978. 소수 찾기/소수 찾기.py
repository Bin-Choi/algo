N = int(input())
n = list(map(int, input().split()))
stk = []
for i in n:
    if i == 1:
        continue
    if i == 2:
        stk.append(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    if i % j == 0:
        continue
    stk.append(i)

print(len(stk))