import  sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    M = int(input())
    cnts = [0] * 200
    ans = 0

    # M명에 대해 빈도수 표시
    for _ in range(M):
        S, E = map(int, input().split())
        # S > E 인 경우에는 빈도수 표시가 안됨
        if S > E:
            S, E = E , S

    # 최대값 찾기
        for i in range((S-1)//2, (E-1)//2+1):
            cnts[i] += 1
        for n in cnts:
            if ans<n:
                ans = n
    print(f'#{test_case} {ans}')