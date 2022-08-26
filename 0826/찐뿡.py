import sys
sys.stdin = open("input.txt", "r")

lst = []
for _ in range(1000):
    lst.append(input())

for i in range(1000):
    string = input()
    if string != lst[i]:
        print(string)
        break