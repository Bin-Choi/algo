import sys
sys.stdin =open("input.txt" , "r")

T = int(input())
for test_case in range(1, T+1):
    str = input()
    stk = []

    for c in str:
        if len(stk) == 0:
            stk.append(c)
        elif c == stk[-1]:
            stk.pop()
        else:
            stk.append(c)

    print(f'#{test_case} {len(stk)}')





