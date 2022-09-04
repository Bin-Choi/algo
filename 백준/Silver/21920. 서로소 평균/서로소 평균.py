import math

n = int(input())
lst = list(map(int, input().split()))
x = int(input())
sum = cnt = 0
dp = [0] * 1000001

for num in lst:
    if dp[num] == 0:
        if math.gcd(num, x) == 1:
            dp[num] = 1
            sum += num
            cnt += 1
        else:
            dp[num] = 2

    elif dp[num] == 1:
        sum += num
        cnt += 1

print(sum/cnt)