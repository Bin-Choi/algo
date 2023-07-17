import sys
sys.stdin = open("input.txt", "r")


def sum_num(code):
    cnt = 0
    for c in code:
        if 'A' <= c <= 'Z':
            pass
        else:
            cnt += int(c)
    return cnt


N = int(input())
arr = []
for i in range(N):
    code = input()
    arr.append(code)

arr.sort(key = lambda x: (len(x), sum_num(x), x))

for i in arr:
    print(i)
    