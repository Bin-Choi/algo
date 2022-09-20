import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    _, st = input().split()

    ans = []
    # [1] 16진수를 10진수 숫자 n에 저장
    for ch in st:
        if '0' <= ch <= '9':
            n = ord(ch)-ord('0')
        else:
            n = ord(ch)-ord('A')+10

        # [2] bit 값 저장
        for i in range(3,-1,-1):
            ans.append((n>>i)&1)

    print(f'#{test_case} {"".join(map(str,ans))}')