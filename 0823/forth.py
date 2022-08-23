import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    equ = input().split()
    stk = []

    for c in equ:
        if c.isdigit():
            stk.append(int(c))
        else:
            try:
                if c == '.':
                    ans = stk.pop()
                else:
                    op2 = stk.pop()
                    op1 = stk.pop()
                    if c == '+':
                        stk.append(op1+op2)
                    elif c == '-':
                        stk.append(op1-op2)
                    elif c == '*':
                        stk.append(op1*op2)
                    elif c == '/':
                        stk.append(op1//op2)
                    else:
                        ans = 'error'
                        break
            except:
                ans = 'error'
                break
    if stk:
        ans = 'error'

    print(f'#{test_case} {ans}')



