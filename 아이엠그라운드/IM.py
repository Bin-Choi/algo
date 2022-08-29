import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, k1, k2 = map(int, input().split())
    cnt = [0] * 101
    people = list(map(int, input().split()))
    lst = []
    for i in people:
        cnt[i] += 1
    for c in range(101):
        if cnt[c] != 0:
            lst.append(cnt[c])
    A = B = C = err = 0
    ans = ans1 = ans2 = 100

    for l in lst:
        if l > k2:
            err = -1

    for i in range(0, len(lst)-2):
        if err == -1:
            print(err)
            break
        A += lst[i]
        B = 0
        if k1 <= A <= k2:
            for j in range(i+1, len(lst)-1):
                B += lst[j]
                C = 0
                if k1 <= B <= k2:
                    for k in range(j+1, len(lst)):
                        C += lst[k]
                        if k1 <= C <= k2:
                            if A + B + C == N:
                                A1 = A
                                B1 = B
                                C1 = C
                                m1 = max(A1, B1, C1)
                                m2 = min(A1, B1, C1)
                                if ans >= m1-m2:
                                    ans = m1-m2
                    if ans1 >= ans:
                        ans1 = ans
        if ans2 >= ans1:
            ans2 = ans1
    if ans2 == 100:
        print(-1)
    else:
        print(ans2)

    # if A == 0 and B == 0 and C == 0:
    #     print(-1)
    # else:
    #     print(ans)






