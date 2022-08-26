import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    Str = input()
    lst = []
    cnt_H = [0] * 14
    cnt_S = [0] * 14
    cnt_D = [0] * 14
    cnt_C = [0] * 14
    ans = ''
    h1 = s1 = d1 = c1 = 0

    for div in range(len(Str)//3):  # 카드 나누기
        lst.append(Str[:3])
        Str = Str[3:]

    for card in lst:
        if card[0] == 'H':
            card = int(card[1:])
            cnt_H[card] += 1
            h1 += 1
            if 2 in cnt_H:
                ans = 1
                break

        elif card[0] == 'S':
            card = int(card[1:])
            cnt_S[card] += 1
            s1 += 1
            if 2 in cnt_S:
                ans = 1
                break

        elif card[0] == 'D':
            card = int(card[1:])
            cnt_D[card] += 1
            d1 += 1
            if 2 in cnt_D:
                ans = 1
                break

        elif card[0] == 'C':
            card = int(card[1:])
            cnt_C[card] += 1
            c1 += 1
            if 2 in cnt_C:
                ans = 1
                break

    if ans == 1:
        print(f'#{test_case} {"ERROR"}')
    else:
        print(f'#{test_case} {13-s1} {13-d1} {13-h1} {13-c1}')


