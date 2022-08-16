import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    max = 0
    str1 = input()
    str2 = input()
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if max < cnt:
            max = cnt

    print(f'#{test_case} {max}')