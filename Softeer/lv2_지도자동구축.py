import sys
sys.stdin = open("input.txt", "r")

N = int(input())

print((2**N+1)**2)
