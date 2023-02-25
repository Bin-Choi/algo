import sys
sys.stdin = open("input.txt", "r")

N = int(input())

for _ in range(N):
    vps = input()
    stk = []
    for c in vps:
        if c == '(':
            stk.append(c)
        elif c == ')':
            if stk:
                stk.pop()
            else:
                print('NO')
                break
    else:
        if not stk:
            print("YES")
        else:
            print("NO")