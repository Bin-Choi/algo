N = int(input())
i = 2
while i <= N:
    if N == 1:
        break
    if N % i == 0:
        print(i)
        N = N//i
    else:
        i += 1
