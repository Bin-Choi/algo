import sys

# 입력
# n: 자동차 대수 q: 테스트 횟수
# 자동차 연비 list 로 주어짐
# 목표 중앙 값 m (q 만큼)

# 출력
# 목표 중앙 값을 만드는 경우의 수

n, q = map(int, input().split())
lst = list(map(int, input().split()))
# 파이썬 sort 는 팀소트 ( nlog(n)
lst.sort()

mn = lst[0]
mx = lst[-1]
# q만큼 시행
for test in range(q):
    # m = 목표값
    m = int(input())
    # m이 최소, 최대 값이면 조합 불가!
    if m == mn or m == mx:
        cnt = 0
    # idx 값을 찾아서 앞 * 뒤 = 경우의 수
    else:
        for i in range(1, n-1):
            if lst[i] == m:
                cnt = i * (n-1-i)
    print(cnt)

