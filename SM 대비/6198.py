import sys
sys.stdin = open("input.txt", "r")

N = int(input())
stack = []
towers = []
cnt = 0
for i in range(N):
    towers.append(int(input()))

for tower in towers:
    while stack and stack[-1] <= tower:
        stack.pop()
    stack.append(tower)

    cnt += len(stack)-1

print(cnt)