import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
que = []

for _ in range(N):
    command = (sys.stdin.readline().split())
    if command[0] == 'push':
        que.append(command[1])

    elif command[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(que))

    elif command[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    else:
        if que:
            print(que[0])
            que = que[1:]
        else:
            print(-1)
