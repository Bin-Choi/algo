import sys
sys.stdin = open("input.txt", "r")


pri = {'(': 1,'+': 2, '*': 3, ')': 4}
T = 10
# T = int(input())
for test_case in range(1, T + 1):
    _ = input()
    st = input()

    equ = ''
    stk = []
    # [1] 중위표기식 -> 후위표기식
    for ch in st:
        if ch.isdigit():  # 숫자인 경우: equ에 추가
            equ += ch
        else:  # 연산자인 경우
            if ch == ')':
                while stk and stk[-1] == '(':
                    equ += stk.pop()

            while stk and pri[ch] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)

    # 잊지말고 처리: 남은 연산자를 순서대로 pop, equ에 추가
    while stk:
        equ += stk.pop()
    if stk and stk[-1] == '(':
        equ.pop()

    print(equ)

    # # [2] 후위표기식 계산
    # for ch in equ:
    #     if ch.isdigit():
    #         stk.append(int(ch))
    #     else:
    #         op2 = stk.pop()
    #         op1 = stk.pop()
    #         if ch == '+':
    #             stk.append(op1 + op2)
    #         elif ch == '*':
    #             stk.append(op1 * op2)
    #
    # print(f'#{test_case} {stk.pop()}')