import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    ans = 0
    box.sort()
    truck.sort()

    while truck and box:
        t = truck.pop()
        b = box.pop()
        if t >= b:
            ans += b
        else:
            truck.append(t)

    print(f'#{test_case} {ans}')


