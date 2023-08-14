import sys
from sys import stdin
import heapq
sys.stdin = open("input.txt", "r")

n, m = map(int, stdin.readline().split())

cards = [int(x) for x in stdin.readline().split()]
heapq.heapify(cards)


for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))

