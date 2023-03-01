import sys
sys.stdin = open("input.txt", "r")

stk = []
res = 1 # result에 더해주기 전 임시 변수
result = 0

lis = list(input())

for i in range(len(lis)):
    if lis[i] == '(':
        res *= 2
        stk.append(lis[i])

    elif lis[i] == '[':
        res *= 3
        stk.append(lis[i])

    elif lis[i] == ')':
        if not stk or stk[-1] != '(':
            result = 0
            break
        if lis[i-1] == '(':
            result += res
            res //= 2
            stk.pop()

    elif lis[i] == ']':
        if not stk or stk[-1] != '[':
            result = 0
            break
        if lis[i-1] == '[':
            result += res
            res //= 3
            stk.pop()
    print(stk)
if stk:
    print(0)
else:
    print(result)

#
#
stack = []  # 스택
res = 1  # result에 더해주기 전 임시 변수
result = 0  # 결과 변수
p = list(input())  # 입력값

# 1~4번째 과정 시작
for i in range(len(p)):
    if p[i] == '(':
        res *= 2
        stack.append(p[i])

    elif p[i] == '[':
        res *= 3
        stack.append(p[i])

    elif p[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if p[i - 1] == '(':
            result += res
        res //= 2
        stack.pop()

    elif p[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if p[i - 1] == '[':
            result += res
        res //= 3
        stack.pop()

# 결과 출력
if stack:
    print(0)
else:
    print(result)