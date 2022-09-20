import sys
sys.stdin = open("input.txt", "r")

dct = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
T = int(input())
for test_case in range(1, T+1):
    st1 = input()
    st2 = ''
    for ch in st1:
        st2 += dct[ch]

    ans = []
    n = 0
    for i in range(len(st2)):
        n = int(st2[i]) + n*2
        # 매 7비트마다 또는 마지막 자리라면
        if (i%7)==6 or i==len(st2)-1:
            ans.append(n)
            n=0

    print(f'#{test_case}', *ans)