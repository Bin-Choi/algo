def pn(a):
    if a < 2:
        return False

    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True


N = int(input())
for n in range(N):
    m = int(input())
    while True:
        if pn(m) == True:
            print(m)
            break
        else:
            m += 1