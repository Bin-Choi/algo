import sys
sys.stdin = open("input.txt", "r")

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for num in B:
    s, e = 0, N - 1     # s는 맨 앞, e는 맨 뒤
    isExist = False       # 찾음 여부

    # 이분탐색 시작
    while s <= e:     # s가 e보다 커지면 반복문 탈출
        m = (s + e)//2  # m는 s,e의 중간값
        if num == A[m]:  # num(목표값)이 A[mid]값과 같다면
            isExist = True
            print(1)
            break
        elif num > A[m]:     # A[m]이 num 보다 작으면
            s = m + 1           # s를 높임
        else:               # A[m]이 num 보다 크다면
            e = m - 1       # e를 낮춤

    if not isExist:          # 없으면 0
        print(0)





