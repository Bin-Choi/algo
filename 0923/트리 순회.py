import sys
sys.stdin = open("input.txt", "r")


N = int(input())
node = {}
for _ in range(N):
    P, L, R = map(str, input().split())
    node[P] = L, R

def front(x):
    left, rigth = node[x][0], node[x][1]
    print(x, end='')
    if left != '.':
        front(left)
    if rigth != '.':
        front(rigth)

def mid(x):
    left, rigth = node[x][0], node[x][1]

    if left != '.':
        mid(left)
    print(x, end='')
    if rigth != '.':
        mid(rigth)

def end(x):
    left, rigth = node[x][0], node[x][1]
    if left != '.':
        end(left)
    if rigth != '.':
        end(rigth)
    print(x, end='')


front('A')
print()
mid('A')
print()
end('A')
print()
