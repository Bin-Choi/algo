import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(T):
    
    DAY = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    m, d = map(int, input().split())
    day = 0

    if m == 1:
        day = d
    else:
        for i in range(1, m):
            if i == 2:
                day += 28
            elif i == 4 or i == 6 or i == 9 or i == 11:
                day += 30
            else:
                day += 31
        day += d

    ans = day%7

    print(DAY[ans])







