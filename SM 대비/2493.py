# N = int(input())
# towers = list(map(int, input().split()))
# stack1 = []
# stack2 = towers[::-1]
# ans = []
# for j in range(N):
#     if len(stack1) == 0:
#         stack1.append(stack2.pop())
#         ans.append(0)
#     else:
#         stack1.append(stack2.pop())
#         k = len(stack1)
#         for i in range(k):
#             if stack1[k-1] < stack1[k-1-i]:
#
#                 ans.append(k-i)
#                 break
#         else:
#             ans.append(0)
#
#
# print(ans)        완전탐색 -> 시간초과
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
towers = list(map(int, input().split()))
stack = []
ans = [0] * N
for n in range(N):
    while stack:
        if towers[stack[-1][0]] < towers[n]:
            stack.pop()
        else:
            ans[n] = stack[-1][0]+1
            break
    stack.append((n, towers[n]))

print(*ans)

# I LOVE YOU <3