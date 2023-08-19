import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())


result = 1
for i in range(k):
    result *= n
    n -= 1

divisior = 1
for i in range(2, k+1):
    divisior *= i

print((result // divisior) % 10007)






