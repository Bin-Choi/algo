import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for time in range(T):
    answer = input()
    score = 0
    add = 1
    for c in answer:
        if c == 'O':
            score += add
            add += 1
        else:
            add = 1
    print(score)

