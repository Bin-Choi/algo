import sys
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())
notebook = [[0]*M for _ in range(N)]
stickers = [{} for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    sticker.append((r, c))
