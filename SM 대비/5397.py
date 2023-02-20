import sys
# sys.stdin = open("input.txt", "r")

Time = int(input())

for test in range(Time):
    command = list(sys.stdin.readline().rstrip())
    stack_1 = []
    stack_2 = []

    for c in command:
        if c == '<':
            if stack_1:
                stack_2.append(stack_1.pop())
        elif c == '>':
            if stack_2:
                stack_1.append(stack_2.pop())
        elif c == '-':
            if stack_1:
                stack_1.pop()
        else:
            stack_1.append(c)

    print(''.join(stack_1 + list(reversed(stack_2))))


