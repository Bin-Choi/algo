import sys
sys.stdin = open("input.txt", "r")

n = int(input())

line = 0
max_num = 0
while n > max_num:

    line += 1
    max_num += line

gap = max_num - n
if line % 2 == 0:
    top = line - gap
    under = gap + 1
else:
    top = gap + 1
    under = line - gap


print(f'{top}/{under}')