import sys
sys.stdin = open("input.txt", "r")

N = int(input())
members = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    members.append((age, name))

members.sort(key = lambda x : x[0])

for i in members:
    print(i[0], i[1])
