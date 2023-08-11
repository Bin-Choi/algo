import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = [list(map(int, input().split())) for _ in range(3)]

total_score = [0] * N

for i in range(len(lst)):
    result = []  # 각 대회의 등수 결과를 저장할 리스트

    for a in range(N):
        rank = 1
        total_score[a] += lst[i][a]
        for b in range(N):
            if lst[i][a] < lst[i][b]:
                rank += 1
        result.append(rank)
    print(*result)








