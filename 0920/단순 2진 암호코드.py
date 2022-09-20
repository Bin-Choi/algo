import sys
sys.stdin = open("input.txt", "r")

dct = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    for n in range(N):
        st = input()
        if '1' in st:
            st1 = st

    e = M-1
    while st1[e] == '0':
        e -= 1

    code = []
    for i in range((e-55),e,7):
        code.append(dct[st1[i:i+7]])

    ans = 0
    for i in range(1, 8):
        if i%2 == 0:

            ans += code[i-1]
        else:
            ans += code[i-1]*3

    ans += code[7]
    if ans%10 == 0:
        ans = sum(code)
    else:
        ans = 0
    print(f'#{test_case}', ans)