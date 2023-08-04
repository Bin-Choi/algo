import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

setting = [0] * 100
test = [0] * 100
start = 0
t_start = 0
for i in range(N):
    end, speed = map(int, input().split())
    end = end
    end = start + end
    for j in range(start, end):
        setting[j] = speed
    start = end

for i in range(M):
    t_end, t_speed = map(int, input().split())
    t_end = t_end
    t_end = t_start + t_end
    for j in range(t_start, t_end):
        setting[j] -= t_speed
    t_start = t_end

ans = min(setting)
if ans >= 0:
    print(0)
else:
    print(abs(ans))

