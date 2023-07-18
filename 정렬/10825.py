import sys
sys.stdin = open("input.txt", "r")

N = int(input())
students = []

for i in range(N):
    name, k, e, m = map(str, input().split())
    students.append([name, int(k), int(e), int(m)])

students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in students:
    print(i[0])