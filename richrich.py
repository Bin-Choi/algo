import sys
sys.stdin =open("input.txt" , "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lis = list(map(int,input().split()))
    profit = cost = cnt = max_cost = sellday = 0
    j = int(0)
    while j < N:
        for i in range(len(lis)):           #최대값 & idx 찾기
            if lis[i] > max_cost:
                max_cost = lis[i]
                sellday = i

        for i in range(sellday):            #최대값 전까지 다 사기
            cnt += 1
            cost += lis[i]

        j += sellday                        #최대값 idx로 이동, 샀던거 다 팔기 & 초기화
        profit += (max_cost * cnt) - cost
        cnt = cost = max_cost = 0

        lis[:] = lis[sellday+1:]            #리스트 슬라이싱
        j += 1

    print(f'#{test_case} {profit}')

            # for j in range(i, N):
            #     if lis[j] > max_cost:
            #         max_cost = lis[j]
        #
        # if lis[i] < max_cost:
        #     cnt += 1
        #     cost += lis[i]
        #
        # else:
        #     profit += (max_cost * cnt) - cost
        #     cnt = cost = 0




