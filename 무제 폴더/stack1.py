import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []
    ans = 1
    for ch in st:
        if ch == '(' or ch == '{':
            stk.append(ch)
        elif ch == ')' and stk[-1] == '(':
            if stk:
                stk.pop()
            else:
                ans = 0
                break
        elif ch == '}' and stk[-1] == '{':
            if stk:
                stk.pop()
            else:
                ans = 0
                break
    print(stk)
        # else:
        #     ans = 0
        #     break
    if stk:
        ans = 0

    print(f'#{test_case} {ans}')
