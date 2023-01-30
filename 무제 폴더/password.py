import sys
sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    N, M = input().split()
    nums = list(map(str, M))
    stk = []

    for i in range(int(N)):
        if not stk:
            stk.append(nums[i])
        else:
            if stk[-1] == nums[i]:
                stk.pop()
            else:
                stk.append(nums[i])

    #     if stk:
    #         if nums[i] == stk[-1]:
    #             stk.pop()
    #         else:
    #             stk.append(nums[i])
    #
    #     else:
    #         stk.append(nums[i])
    #
    print(f'#{test_case}', ''.join(stk))
