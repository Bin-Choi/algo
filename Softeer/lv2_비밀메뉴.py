import sys
sys.stdin = open("input.txt", "r")

M, N, K = map(int, input().split())

secret = input().replace(" ", "")
code = input().replace(" ", "")

if secret in code:
    print("secret")
else:
    print("normal")

