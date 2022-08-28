import sys

sys.stdin = open("input.txt", "r")

mans = []
sum = 0
for c in range(9):
    mans.append(int(input()))
    sum += mans[c]
over = sum - 100



for i in range(8):
    for j in range(1 + i, 9):
        if mans[i] + mans[j] == over:
            m1 = i
            m2 = j

mans[m1] = mans[m2] = 0
mans.sort()
for man in range(2, 9):
    print(mans[man])


