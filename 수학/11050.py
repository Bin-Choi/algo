import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())


def bino_coef(n, k):
    if k > n:
        return 0

    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def choose(times, got):

        if times == n:
            return got == k

        if cache[times][got] != -1:
            return cache[times][got]

        cache[times][got] = choose(times+1, got) + choose(times+1, got +1)

        return cache[times][got]

    return choose(0,0)


print(bino_coef(n, m))