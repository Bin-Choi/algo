import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
start = 1
stack = []
command = []
temp = True
for _ in range(N):
    n = int(sys.stdin.readline())
    while n >= start:
        stack.append(start)
        command.append('+')
        start += 1
    if stack[-1] == n:
        stack.pop()
        command.append('-')
    else:
        temp = False
        break

if not temp:
    print("NO")
else:
    for i in command:
        print(i)





