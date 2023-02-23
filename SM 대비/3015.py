import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
ans = 0

for a in arr:
    while stack and stack[-1][0] < a:
        ans += stack.pop()[1]

    if not stack:
        stack.append((a, 1))
        continue

    if stack[-1][0] == a:
        cnt = stack.pop()[1]
        ans += cnt

        if stack:
            ans += 1

        stack.append((a, cnt+1))
    else:
        stack.append((a, 1))
        ans += 1

print(ans)

# lst = [int(input()) for _ in range(int(input()))]
#
# stack = []
# ans = 0
#
# for l in lst:
#     while stack and stack[-1][0] < l:
#         ans += stack.pop()[1]
#
#     if not stack:
#         stack.append((l, 1))
#         continue
#
#     if stack[-1][0] == l:
#         cnt = stack.pop()[1]
#         ans += cnt
#
#         if stack:
#             ans += 1
#             stack.append((l, cnt+1))
#
#     else:
#         stack.append((l, 1))
#         ans += 1
#
# print(ans)

