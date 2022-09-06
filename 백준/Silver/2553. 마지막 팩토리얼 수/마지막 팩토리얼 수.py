import math

N = int(input())
num = math.factorial(N)
num = str(num)
l = len(num)

for i in range(l-1, -1, -1):
    if num[i] != "0":
        print(num[i])
        break