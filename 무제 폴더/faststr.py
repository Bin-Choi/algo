import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    str1, str2 = map(str, input().split())
    N = len(str1)
    M = len(str2)
    min = i = 0
    while i < N:
        if str1[i:i+M] == str2[:]:
            min += 1
            i += M
        else:
            min += 1
            i += 1

    print(f'#{test_case} {min}')