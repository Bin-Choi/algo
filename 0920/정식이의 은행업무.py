import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    two = list(input())
    three = list(input())
    check = 0  # breakpoint

    for i in range(len(two)*2): #이진법
        Two = two[:]
        Two[i//2] = str(i % 2)
        a = ''.join(Two)

        for j in range(len(three)*3):
            Three = three[:]
            Three[j//3] = str(j % 3)
            b = ''.join(Three)
            if int(a, 2) == int(b, 3):
                print(f'#{test_case} {int(a,2)}')
                check = 1
                break
        if check == 1:
            break