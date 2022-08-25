import sys
sys.stdin = open("input.txt", "r")

# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] q 생성 후 순서대로 피자 가득 채움
    q = []
    for i in range(N):
        q.append((i+1, lst[i]))

    # for 문을 나왔을때 i 값은 N-1 이므로로
   i = N

    # [2] q 가 not empty 일 동안 루프
    while q:
        ans, piz = q.pop(0)    # 피자번호, 치즈량
        piz //= 2

        if piz == 0:    # 꺼내는 경우
            if i < M:    # 넣을 피자가 있는 경우
                q.append((i+1, lst[i]))
                i += 1
        else:
            q.append((ans, piz))

    print(f'#{test_case} {ans}')
