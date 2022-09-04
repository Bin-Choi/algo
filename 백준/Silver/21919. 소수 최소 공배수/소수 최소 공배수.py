N = int(input())
lst = list(map(int, input().split()))
ans = []

for i in range(N):
    if lst[i] == 2 or lst[i] == 3:
        ans.append(lst[i])
    else:
        for j in range(2, int(lst[i]**0.5)+1):
            if lst[i] % j == 0:
                break

        if lst[i] % j != 0:
            ans.append(lst[i])

if ans:
    a = 1
    for i in ans:
        if a % i != 0:
            a *= i
    print(a)

else:
    print(-1)