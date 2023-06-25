import sys
sys.stdin = open("input.txt", "r")


def hanoi(N, start, end):
    if N == 1:
        print(start, end)
        return

    hanoi(N-1, start, 6-start-end)  # 1단계, 탑의 수는 3개이므로 (1, 2, 3) 모두 합치면 6이 된다. 즉, 중간 목적지는 6-start-end
    print(start, end)  # 2단계
    hanoi(N-1, 6-start-end, end)  # 3단계


n = int(input())
print(2**n-1)
hanoi(n, 1, 3)

# 이동 거리 구하는 방법은 점화식을 활용