import sys
sys.stdin = open("input.txt", "r")

N = int(input())
nums = list(map(int, input().split()))

for i in range(1, N):
    nums[i] = max(nums[i-1], 0) + nums[i]

print(max(nums))



