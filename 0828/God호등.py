import sys
sys.stdin = open("input.txt", "r")

T, L = map(int, input().split())
time = 0
for t in range(T):
    D, R, G = map(int, input().split())
    if (time + D) % (R + G) < R:
        time += R - ((time + D) % (R + G))

print(time+L)
