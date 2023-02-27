import sys
sys.stdin = open("input.txt", "r")

s = input()

stk = []
cnt = 0
ans = 0
for i in s:
    if len(stk) == 0:
        stk.append(i)
        cnt += 1

    else:
        if i == ')':
            if stk[-1] == '(':
                cnt -= 1
                ans += cnt
                stk.append(i)

            elif stk[-1] == ')':
                cnt -= 1
                ans += 1
                stk.append(i)
        elif i == '(':
            cnt += 1
            stk.append(i)

print(ans)