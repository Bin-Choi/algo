import sys
import heapq
sys.stdin = open("input.txt", "r")

q = []
N = int(input())
for i in range(N):
    s, t = map(int, input().split())
    q.append([s, t])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, N):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))




