import sys

sys.stdin = open("input.txt", "r")

N = int(input())
ans = 0
for _ in range(N):
    stk = []
    word = input()

    for w in word:
        if len(stk) == 0:
            stk.append(w)
        else:
            if w == 'A':
                if stk[-1] == 'A':
                    stk.pop()
                elif stk[-1] == 'B':
                    stk.append(w)

            elif w == 'B':
                if stk[-1] == 'A':
                    stk.append(w)
                elif stk[-1] == 'B':
                    stk.pop()

    if len(stk) == 0:
        ans += 1

print(ans)