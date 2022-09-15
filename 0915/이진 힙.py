import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # [1] 힙에 데이터 추가 and 최소힙 유지
    heap = [0]*(N+1)
    last = 0
    for n in lst:
        last += 1
        heap[last] = n

        # 부모가 존재하고, 부모가 나보다 큰 경우: 교환
        c = last
        while c//2 and heap[c]<heap[c//2]:
            heap[c], heap[c//2] = heap[c//2], heap[c]
            c //= 2

        #[2] Last 의 조상노드들의 합
    ans = 0
    c = last//2
    while c:
        ans += heap[c]
        c //= 2

    print('#{} {}'.format(test_case, ans))