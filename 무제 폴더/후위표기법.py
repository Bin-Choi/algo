import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    Str = input()
    result = []
    stk = []
    ref = {'+': 1, '*': 2}          # 연산자 우선도 참조용 dic

    for s in Str:
        if s.isdigit():             # 숫자 바로 추가
            result.append(s)
        else:                                           # 연산자 ..
            while stk and ref[s] <= ref[stk[-1]]:       # 스택이 비거나 현재 연산자보다 스택 마지막 연산자의 우선순위가 높을때까지
                result.append(stk.pop())                # 스택의 연산자를 추출 & 결과에 추가

            stk.append(s)                               # 아닐 경우, 추가

    while stk:                                          # 스택이 빌 때까지
        result.append(stk.pop())                        # 스택의 마지막 요소를 추출, 결과에 추가

    print(f'#{test_case} {"".join(result)}')
