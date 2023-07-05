import sys
sys.stdin = open("input.txt", "r")
ans = []


def dfs(start):
    if len(ans) == 6:
        print(*ans)
        return

    for i in range(start, length):
        if not nums[i] in ans:
            ans.append(nums[i])
            dfs(i)
            ans.pop()


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break

    length = nums.pop(0)

    visited = [0] * len(nums)
    dfs(0)

    print(' ')
