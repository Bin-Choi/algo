# 회문
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    ans = ""
    arr = [input() for _ in range(N)]

    for row in arr:
        for i in range(N-M+1):
            if row[i:i+M] == row[i:i+M][::-1]:
                ans = ''.join(row[i:i+M])

    for col in list(map(list, zip(*arr))):
        for j in range(N-M+1):
            if col[j:j+M] == col[j:j+M][::-1]:
                ans = ''.join(col[j:j+M])

    print(f'#{test_case} {ans}')