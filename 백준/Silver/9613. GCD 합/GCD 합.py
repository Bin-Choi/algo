import math

T = int(input())
for test_case in range(T):
    lst = list(map(int, input().split()))
    lst.pop(0)
    N = len(lst)
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += math.gcd(lst[i], lst[j])
    print(ans)