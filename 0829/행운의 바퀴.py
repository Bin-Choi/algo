import sys
sys.stdin = open("input.txt", "r")

L, N = map(int, input().split())
ans = ['?']*L
x = err = 0
stk = []
st = []
for n in range(N):
    i, j = map(str, input().split())
    i = int(i)
    stk.append(i)
    st.append(j)

ans[0] = st.pop()
for k in range(N-1):
    x = (stk.pop()+x)%L
    y = st.pop()
    if ans[x%L] != '?' and ans[x%L] != y:
        err = 1

    ans[x % L] = y

for z in range(L-1):
    for v in range(z+1, L):
        if ans[z] == ans[v] and ans[z] != '?' and ans[v] != '?':
            err = 1

if err == 1:
    print('!')
else:
    print(''.join(ans))






