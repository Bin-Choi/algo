import sys
sys.stdin = open('input.txt', 'r')


def move():
    dr = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    revers_dr = [0, 2, 1, 4, 3]
    check = {}

    for k in range(K):
        group = arr[k]
        i, j, size, d = group

        if size == 0:
            continue

        ni = i + dr[d][0]
        nj = j + dr[d][1]
        group[0], group[1] = ni, nj

        if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
            group[2] //= 2
            group[3] = revers_dr[d]

        if (ni, nj) not in check:
            check[ni, nj] = (k, size)
            continue

        n_k, n_size = check[(ni, nj)]
        if size > n_size:
            group[2] += arr[n_k][2]
            check[(ni, nj)] = (k, size)
            arr[n_k][2] = 0
        else:
            arr[n_k][2] += size
            group[2] = 0


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        move()

    ans = 0

    for q in range(K):
        ans += arr[q][2]

    print(f'#{test_case} {ans}')
