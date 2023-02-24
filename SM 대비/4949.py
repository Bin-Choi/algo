import sys
sys.stdin = open("input.txt", "r")

while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = True

    for i in s:
        if i == '(' or i == '[':
            stk.append(i)

        elif i == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                temp = False
                break
        elif i == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                temp = False
                break

    if temp == True and not stk:
        print('yes')
    else:
        print('no')
