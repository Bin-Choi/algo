for _ in range(10):
    tc = int(input())
    lst = list(map(int, input().split()))

tmp = i = 1
while tmp != 0:
    tmp = lst.pop(0) - i
    if tmp <= 0:
        t = 0
    lst.append(t)
    i = (i % 5) + 1
print(f'#{}')