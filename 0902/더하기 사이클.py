import sys
sys.stdin = open("input.txt", "r")


def new_num(n):
    a = n // 10
    b = n % 10
    new = (10*b)+(a+b)%10
    return new


N = int(input())
New = N
cnt = 0
while True:
    if New < 10:
        New = New*10
        print(New)
    else:
        New = new_num(New)
        if New < 10:
            New = New*10
        cnt += 1
        print(New, cnt)
    if New == N:
        break
print(cnt)
