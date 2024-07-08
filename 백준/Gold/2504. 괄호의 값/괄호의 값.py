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
        
if stk:
    print(0)
else:
    print(result)
