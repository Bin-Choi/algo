import sys
sys.stdin = open("input.txt", "r")

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in alpha:
    if i in s:
        s = s.replace(i, "*")

print(len(s))