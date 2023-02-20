import sys
sys.stdin = open("input.txt", "r")

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
N = len(stack1)
M = int(input())

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == "L" and stack1:
        stack2.append(stack1.pop())
    elif command[0] == "D" and stack2:
        stack1.append(stack2.pop())
    elif command[0] == "B" and stack1:
        stack1.pop()
    elif command[0] == "P":
        stack1.append(command[1])

print("".join(stack1 + list(reversed(stack2))))